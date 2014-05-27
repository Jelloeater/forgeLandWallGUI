from Tkinter import *
import logging
import tkMessageBox

from controler import messageController
# from settings import editSettings


class bootloader(messageController):
	def __init__(self):
		pass

	@classmethod
	def startUp(cls):
		logging.debug('Started Boot loader')

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
			cls.loadSettings()
			cls.refreshMessageList()

	@classmethod
	def runMain(cls):
		cls.root = Tk()
		cls.root.columnconfigure(0, weight=1)
		# root.rowconfigure(0, weight=1)
		cls.root.geometry("300x250")
		cls.root.minsize(width=300, height=200)
		cls.root.title('Forge Land Message Editor ' + mainGUI.versionNumber)
		cls.root.wm_iconbitmap(bitmap='images/icon.ico')
		mainGUI(cls.root).grid()
		cls.root.mainloop()

	@classmethod
	def shutDown(cls):
		logging.debug('Shutting down')
		cls.saveSettings()


class mainGUI(Frame, messageController, bootloader):
	def __init__(self, rootWindow):
		Frame.__init__(self, self.root)

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
		self.optionsMenu.add_command(label="Refresh", command=self.refreshGUI, underline=1)
		self.optionsMenu.add_command(label="Settings", command=self.editSettings, underline=1)
		self.helpMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
		self.helpMenu.add_command(label="Help", command=self.programHelp, underline=1)
		self.helpMenu.add_command(label="About", command=self.aboutBox, underline=1)
		self.master.config(menu=self.menuBar)


		self.topFrame = Frame()
		self.entryBox = Entry(self.topFrame)
		self.entryBox.insert(0, self.defaultMessageBoxText)
		self.entryBox.bind('<Return>', lambda event: self.addMessage_GUI(self.entryBox.get()))
		# Bind needs to send the event to the handler
		self.entryBox.pack(side='left', fill='x', expand='True', padx=5)

		self.addMessage = Button(self.topFrame)
		self.addMessage['text'] = 'Add New Message'
		self.addMessage['command'] = lambda: self.addMessage_GUI(self.entryBox.get())
		self.addMessage.pack(side='left', padx=0)

		self.searchButton = Button(self.topFrame)
		self.searchButton['text'] = 'Search'
		self.searchButton['command'] = lambda: self.searchMessage_GUI(self.entryBox.get())
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

	def messageListBox(self):
		messagesToLoad = self.messageList  # Fetch Message List from model

		for i in messagesToLoad:
			rowToInsertAt = messagesToLoad.index(i)

			messageText = Label(self.messageListFrame)
			messageText['text'] = i['message']
			messageText.grid(column=0, row=rowToInsertAt, sticky='w', padx=0)

			timestampText = Label(self.messageListFrame)
			timestampText['text'] = i['timestamp']
			timestampText.grid(column=1, row=rowToInsertAt, sticky='e', padx=10)

			editButton = Button(self.messageListFrame)
			editButton['text'] = 'Edit'
			editButton['command'] = lambda i=i: self.editMessage_GUI(i)  # Self referencing callback function
			editButton.grid(column=2, row=rowToInsertAt, sticky='e')

			deleteButton = Button(self.messageListFrame)
			deleteButton['text'] = 'Delete'
			deleteButton['command'] = lambda i=i: self.deleteMessage_GUI(i)
			deleteButton.grid(column=3, row=rowToInsertAt, sticky='e', padx=10)
		# logging.debug(i)
		# logging.debug(rowToInsertAt)

	def addMessage_GUI(self, messageToAdd):
		status = self.addMessageToList(messageToAdd)
		if not status:
			tkMessageBox.showerror('Error','Message invalid')
		self.entryBox.select_range(0, END)  # Selects the contents so the user can just type the next message
		self.refreshGUI()

	def editMessage_GUI(self, messageRecordIn):

		def editMessage_GUI_Ok_Command(messageInDialogIn):
			if messageRecordIn['message'] != textBox.get():
				status = self.editMessage(indexToEdit=messageRecordIn['index'], newMessage=textBox.get())
				if not status:
					tkMessageBox.showerror('Error', 'Blank message')
				self.refreshGUI()
			else:
				tkMessageBox.showerror(message='Enter a new message')
			messageInDialogIn.destroy()

		messageInDialog = Tk()
		messageInDialog.title('Edit Message')
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
		self.refreshGUI()

	def searchMessage_GUI(self, messageToSearchFor):
		logging.debug('Refreshing Message Window - Search')
		self.searchMessage(messageToSearchFor)
		self.refresh_GUI_Window()

	def refreshGUI(self):
		""" Refreshes the message list AND GUI window"""
		logging.debug('Refreshing Message Window')
		self.refreshMessageList()
		self.refresh_GUI_Window()

	def refresh_GUI_Window(self):
		""" Refreshes just the GUI window"""
		self.messageListCanvas.destroy()
		self.vsb.destroy()
		self.hsb.destroy()
		self.createMessageFrame()

	def OnFrameConfigure(self, event):
		"""Reset the scroll region to encompass the inner frame"""
		self.messageListCanvas.configure(scrollregion=self.messageListCanvas.bbox("all"))

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