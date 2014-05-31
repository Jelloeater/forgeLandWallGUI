from Tkinter import *
import logging
import tkMessageBox
import os
import threading
import time
from controler import messageController


class bootloader(messageController):
	""" Helps both start AND stop the application """
	def __init__(self):
		messageController.__init__(self)

	@classmethod
	def startUp(cls):
		logging.debug('Started Boot loader')
		cls.loadSettings()
		while not cls.isServerActive():
			top = Tk()
			top.withdraw()
			tkMessageBox.showerror(message='Cannot Reach Server @ ' + 'http://' + cls.serverIp + ':' + cls.port + '/'
			                               + '\nPlease edit server address')
			top.destroy()

			settingsBox = cls.editSettings()
			settingsBox.mainloop()  # This needs to be present or else the program will do a nasty infinite loop
		# We don't need to destroy the window because it will destroy itself when its done,
		# there by exiting the loop and moving forward
		else:
			cls.refreshMessageList()

	@classmethod
	def runMain(cls):
		cls.root = Tk()
		cls.root.columnconfigure(0, weight=1)
		# root.rowconfigure(0, weight=1)
		cls.root.geometry("300x250")
		cls.root.minsize(width=300, height=200)
		cls.root.title('Forge Land Message Editor ' + mainGUI.versionNumber)
		if os.name == "nt":
			cls.root.wm_iconbitmap(bitmap='images/icon.ico')
		cls.mainGUIObj = mainGUI()
		cls.mainGUIObj.grid()
		cls.autoRefresh(cls.mainGUIObj)
		cls.root.mainloop()

	@classmethod
	def shutDown(cls):
		logging.debug('Shutting down')
		cls.saveSettings()

	@classmethod
	def autoRefresh(cls, mainGUIObj):
		""" Starts the refresh background thread """
		def refreshLoop(mainGUIObjRef):
			while True:
				cls.autoRefreshLock.acquire()
				if mainGUIObj.isValidSearch(mainGUIObjRef.searchField):  # Any "valid" search is triggering this, not foud issue
					if not mainGUIObjRef.searchMessage_GUI():
						logging.debug('Auto Searching for: ' + mainGUIObjRef.searchField)
						mainGUIObjRef.searchField = ''
						# Mimics the same behavior as searchFieldSet_GUI
				else:
					logging.debug('Auto Refreshing')
					mainGUIObjRef.refresh_GUI()
				cls.autoRefreshLock.release()
				time.sleep(cls.refreshInterval)

		t = threading.Thread(target=refreshLoop, args=(mainGUIObj,))
		t.daemon = True
		t.start()


class mainGUI(Frame, messageController, bootloader):
	""" Contains the main view for the application """
	def __init__(self):
		""" Create the initial application GUI environment (tool bars, and other static elements) """
		Frame.__init__(self, self.root)
		self.searchField = ''  # Hold both search string, and drives autoRefresh logic

		self.menuBar = Menu()
		self.fileMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="File", menu=self.fileMenu, underline=1)
		self.fileMenu.add_command(label="Quit", command=self.root.destroy, underline=1)

		self.editMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
		self.editMenu.add_command(label="Cut", underline=1)
		self.editMenu.add_command(label="Copy", underline=1)
		self.editMenu.add_command(label="Paste", underline=1)
		# FIXME add working copy paste

		self.optionsMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Options", menu=self.optionsMenu)
		self.optionsMenu.add_command(label="Settings", command=self.editSettings, underline=1)
		self.helpMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
		self.helpMenu.add_command(label="Help", command=self.programHelp, underline=1)
		self.helpMenu.add_command(label="About", command=self.aboutBox, underline=1)
		self.master.config(menu=self.menuBar)

		self.topFrame = Frame()
		self.entryBox = Entry(self.topFrame)
		self.entryBox.insert(0, self.defaultMessageBoxText)
		self.entryBox.bind('<Return>', lambda event: self.addMessage_GUI())
		# Bind needs to send the event to the handler
		self.entryBox.pack(side='left', fill='x', expand='True', padx=5)

		self.addMessage = Button(self.topFrame)
		self.addMessage['text'] = 'Add New Message'
		self.addMessage['command'] = lambda: self.addMessage_GUI()
		self.addMessage.pack(side='left', padx=0)

		self.searchButton = Button(self.topFrame)
		self.searchButton['text'] = 'Search'
		self.searchButton['command'] = lambda: self.searchFieldSet_GUI()
		self.searchButton.pack(side='right', padx=0)

		self.topFrame.pack(fill='x')

		self.createMessageFrame()

	# TODO Add status bar

	# self.statusBar = Frame()
	# self.status = Label(self.statusBar)
	# self.status['text'] = "Ok"
	# self.status.pack(side='bottom', padx=5)
	# self.statusBar.pack(side='bottom', fill='x', expand='True', padx=5)

	# noinspection PyAttributeOutsideInit

	def createMessageFrame(self):
		""" Sets up the main message frame (where the magic happens) """

		# Sets up frame
		self.messageListCanvas = Canvas(self.root, borderwidth=0)
		self.messageListFrame = Frame(self.messageListCanvas)

		# Creates scroll bar
		self.vsb = Scrollbar(self.root, orient="vertical", command=self.messageListCanvas.yview)
		self.messageListCanvas.configure(yscrollcommand=self.vsb.set)
		self.vsb.pack(side="right", fill="y")

		self.hsb = Scrollbar(self.root, orient="horizontal", command=self.messageListCanvas.xview)
		self.messageListCanvas.configure(xscrollcommand=self.hsb.set)
		self.hsb.pack(side="bottom", fill="x")

		# Packs frame
		self.messageListCanvas.pack(side="left", fill="both", expand=True)
		self.messageListCanvas.create_window((4, 4), window=self.messageListFrame, anchor="nw", tags="self.frame")
		self.messageListFrame.bind("<Configure>", self.OnFrameConfigure)

		self.messageListBox()

	def OnFrameConfigure(self, event):
		"""Reset the scroll region to encompass the inner frame"""
		self.messageListCanvas.configure(scrollregion=self.messageListCanvas.bbox("all"))

	def messageListBox(self):
		""" Creates the message list box for the createMessageFrame method """
		messagesToLoad = self.messageList  # Fetch Message List from model

		for i in messagesToLoad:
			rowToInsertAt = messagesToLoad.index(i)

			messageText = Label(self.messageListFrame)
			messageText['text'] = i['message']
			messageText.grid(column=0, row=rowToInsertAt, sticky='w', padx=0)
			# TODO Causing crash when user refreshes too fast ?

			timestampText = Label(self.messageListFrame)
			timestampText['text'] = i['timestamp']
			timestampText.grid(column=1, row=rowToInsertAt, sticky='e', padx=10)

			editButton = Button(self.messageListFrame)
			editButton['text'] = 'Edit'
			editButton['command'] = lambda messageIn=i: self.editMessage_GUI(
				messageIn)  # Self referencing callback function
			editButton.grid(column=2, row=rowToInsertAt, sticky='e')

			deleteButton = Button(self.messageListFrame)
			deleteButton['text'] = 'Delete'
			deleteButton['command'] = lambda messageIn=i: self.deleteMessage_GUI(messageIn)
			deleteButton.grid(column=3, row=rowToInsertAt, sticky='e', padx=10)

	def addMessage_GUI(self):
		# FIXME handle empty new message
		status = self.addMessageToList(self.entryBox.get())
		if not status:
			tkMessageBox.showerror('Error', 'Message invalid')
		self.entryBox.select_range(0, END)  # Selects the contents so the user can just type the next message
		self.refresh_GUI()

	def editMessage_GUI(self, messageRecordIn):
		self.autoRefreshLock.acquire()  # Locks auto refresh to prevent GUI redraw errors

		def editMessage_GUI_Ok_Command(messageInDialogIn):
			if messageRecordIn['message'] != textBox.get():
				status = self.editMessage(indexToEdit=messageRecordIn['index'], newMessage=textBox.get())
				if not status:
					tkMessageBox.showerror('Error', 'Blank message')
				self.refresh_GUI()
			else:
				tkMessageBox.showerror(message='Enter a new message')
			messageInDialogIn.destroy()
			self.autoRefreshLock.release() # Releases lock on edit box exit

		messageInDialog = Tk()
		messageInDialog.title('Edit Message')
		if os.name == "nt":
			messageInDialog.wm_iconbitmap(bitmap='images/icon.ico')
		messageInDialog.columnconfigure(0, weight=1)
		messageInDialog.rowconfigure(0, weight=1)

		messageInDialog.minsize(width=100, height=50)
		frame = Frame(messageInDialog)

		label = Label(frame)
		label['text'] = 'Enter New Message'
		label.pack()

		textBox = Entry(frame)
		textBox.insert(0, messageRecordIn['message'])
		textBox.pack(fill='both')

		submitButton = Button(frame)
		submitButton['text'] = 'Ok'
		submitButton['command'] = lambda: editMessage_GUI_Ok_Command(messageInDialog)
		submitButton.pack(side="left", expand="yes", fill="both", padx=5, pady=3)

		cancelButton = Button(frame)
		cancelButton['text'] = 'Cancel'
		cancelButton['command'] = messageInDialog.destroy
		cancelButton.pack(fill='both', expand="yes", padx=5, pady=3)

		frame.pack(fill='both', expand="yes", padx=0, pady=0)

	def deleteMessage_GUI(self, c):
		self.deleteMessage(indexToDelete=c['index'])
		self.refresh_GUI()

	def searchFieldSet_GUI(self):
		""" Sets self object search field (used by auto refresh) """
		if self.isValidSearch(self.entryBox.get()):
			self.searchField = self.entryBox.get()
			if not self.searchMessage_GUI():  # Runs search query, returns False if nothing found
				tkMessageBox.showwarning(message='No Results Found')
				self.searchField = ''  # Resets search field to empty (which drives auto refresh logic)
				# FIXME Handle no JSON parse
				# self.refresh_GUI()
		else:
			self.refresh_GUI()

	@classmethod
	def isValidSearch(cls, query):
		""" Parses for valid input (we should be taking input, not getting input from elsewhere) """
		if query.isspace() or query == '' or query == cls.defaultMessageBoxText:
			return False
		else:
			return True

	def searchMessage_GUI(self):
		""" End action by either pressing search or auto refresh re-searching again"""
		logging.debug('Refreshing Message Window - Search')
		returnVal = self.searchMessage(self.searchField)
		self.refresh_GUI_Window()
		return returnVal

	def refresh_GUI(self):
		""" Refreshes the message list AND GUI window (used by auto refresh)"""
		self.refreshMessageList()
		self.refresh_GUI_Window()

	def refresh_GUI_Window(self):
		""" Refreshes just the GUI window"""
		self.messageListCanvas.destroy()
		self.vsb.destroy()
		self.hsb.destroy()
		self.createMessageFrame()

	def aboutBox(self):
		message = 'A simple GET/POST front end for a message server API. \nBy Jesse S \n' + self.versionNumber \
		          + '\nhttp://bitbucket.org/Jelloeater/forgelandwallgui'
		tkMessageBox.showinfo(title='About', message=message)

	@staticmethod
	def programHelp():
		message = 'Press button \nReceive message'
		tkMessageBox.showinfo(title='About', message=message)


if __name__ == "__main__":
	logging.debug("Started main program")

	bootloader.startUp()

	bootloader.runMain()

	bootloader.shutDown()
	logging.debug("End Of Program")