from Tkinter import *
import logging
import tkSimpleDialog
import tkMessageBox

from controler import messageController


class main(Frame, messageController):
	def __init__(self, rootWindow):
		Frame.__init__(self, root)

		self.menuBar = Menu()
		self.fileMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="File", menu=self.fileMenu, underline=1)
		self.fileMenu.add_command(label="Quit", command=root.destroy, underline=1)
		self.optionsMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Options", menu=self.optionsMenu)
		self.optionsMenu.add_command(label="Refresh", command=self.refreshGUI, underline=1)
		self.optionsMenu.add_command(label="Server Settings", command=self.editServerAddress, underline=1)
		self.editMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Help", menu=self.editMenu)
		self.editMenu.add_command(label="Help", command=self.programHelp, underline=1)
		self.editMenu.add_command(label="About", command=self.aboutBox, underline=1)
		self.master.config(menu=self.menuBar)

		self.refreshMessageList()

		# TODO Add search function

		self.topFrame = Frame()
		self.entryBox = Entry(self.topFrame)
		self.entryBox.insert(0, self.defaultMessageBoxText)
		self.entryBox.bind('<Return>', lambda event: self.addMessage_GUI(self.entryBox.get()))
		# Bind needs to send the event to the handler
		self.entryBox.pack(side='left', fill='x', expand='True', padx=5)

		self.addMessage = Button(self.topFrame)
		self.addMessage['text'] = 'Add New Message'
		self.addMessage['command'] = lambda: self.addMessage_GUI(self.entryBox.get())
		self.addMessage.pack(side='right', padx=0)
		self.topFrame.pack(fill='x')

		self.createMessageFrame()

		# TODO Add status bar

	# noinspection PyAttributeOutsideInit
	def createMessageFrame(self):
		# Sets up frame
		self.messageListCanvas = Canvas(root, borderwidth=0)
		self.messageListFrame = Frame(self.messageListCanvas)

		# Creates scroll bar
		self.vsb = Scrollbar(root, orient="vertical", command=self.messageListCanvas.yview)
		self.messageListCanvas.configure(yscrollcommand=self.vsb.set)
		self.vsb.pack(side="right", fill="y")

		self.hsb = Scrollbar(root, orient="horizontal", command=self.messageListCanvas.xview)
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

	def editMessage_GUI(self, c):
		messageIn = tkSimpleDialog.askstring(title='Edit message', prompt='Enter new message')
		# TODO Maybe replace with custom dialog box?
		status = self.editMessage(indexToEdit=c['index'], newMessage=messageIn)
		if not status:
			tkMessageBox.showerror('Error', 'Blank message')
		self.refreshGUI()

	def deleteMessage_GUI(self, c):
		self.deleteMessage(indexToDelete=c['index'])
		self.refreshGUI()

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

	def editServerAddress(self):
		# TODO Create GUI w/ address and port, then destroy when done
		pass

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
	root = Tk()
	root.columnconfigure(0, weight=1)
	# root.rowconfigure(0, weight=1)
	root.geometry("300x250")
	root.minsize(width=300, height=200)
	root.title('Forge Land Message Editor ' + main.versionNumber)
	root.wm_iconbitmap(bitmap='images/icon.ico')
	main(root).grid()
	root.mainloop()
	logging.debug("End Of Program")