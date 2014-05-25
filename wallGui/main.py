from Tkinter import *
import logging
from controler import messageController

class main(Frame, messageController):
	def __init__(self, rootWindow):
		Frame.__init__(self, root)

		self.menuBar = Menu()
		fileMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="File", menu=fileMenu, underline=1)
		fileMenu.add_command(label="Quit", command=root.destroy, underline=1)
		optionsMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Options", menu=optionsMenu)
		optionsMenu.add_command(label="Refresh", command=self.refreshWindow, underline=1)
		optionsMenu.add_command(label="Server Settings")
		editMenu = Menu(self.menuBar, tearoff=0)
		self.menuBar.add_cascade(label="Help", menu=editMenu)
		editMenu.add_command(label="Help")
		editMenu.add_command(label="About")
		self.master.config(menu=self.menuBar)

		self.refreshMessageList()

		self.topFrame = Frame()
		entryBox = Entry(self.topFrame)
		entryBox.pack(side='left', fill='x', expand='True')


		addMessage = Button(self.topFrame)
		addMessage['text'] = 'Add New Message'
		# addMessage['command'] = main.refreshMessageList
		addMessage.pack(side='right', padx=10)
		self.topFrame.pack(fill='x')

		self.createMessageFrame()


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
		self.messageListCanvas.create_window((4,4), window=self.messageListFrame, anchor="nw", tags="self.frame")
		self.messageListFrame.bind("<Configure>", self.OnFrameConfigure)

		self.messageListBox()

	def messageListBox(self):

		messagesToLoad = self.messageList # Fetch Message List from model

		# FIXME Get button instances
		# http://tkinter.unpythonic.net/wiki/CallbackConfusion
		# http://stackoverflow.com/questions/728356/dynamically-creating-a-menu-in-tkinter-lambda-expressions
		for i in messagesToLoad:
			rowToInsertAt = messagesToLoad.index(i) + 1

			messageText = Label(self.messageListFrame)
			messageText['text'] = i['message']
			messageText.grid(column=0, row=rowToInsertAt, sticky='w', padx=10)

			timestampText = Label(self.messageListFrame)
			timestampText['text'] = i['timestamp']
			timestampText.grid(column=1, row=rowToInsertAt, sticky='e', padx=10)

			editButton = Button(self.messageListFrame)
			editButton['text'] = 'Edit'
			# editButton['command'] = lambda rowToInsertAt=rowToInsertAt: self.editMessage(messagesToLoad[rowToInsertAt-1])
			editButton['command'] = lambda i=i: self.editMessage(i)
			editButton.grid(column=2, row=rowToInsertAt, sticky='e')

			deleteButton = Button(self.messageListFrame)
			deleteButton['text'] = 'Delete'
			deleteButton['command'] = lambda i=i: self.deleteMessage(i)
			deleteButton.grid(column=3, row=rowToInsertAt, sticky='e', padx=10)
			# logging.debug(i)
			# logging.debug(rowToInsertAt)



	def editMessage(self, c):
		logging.debug('Editing: ' + str(c))
		# TODO Write Edit function

	def deleteMessage(self,c):
		logging.debug('Deleting: ' + str(c))
		# TODO Write Delete Function


	def OnFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.messageListCanvas.configure(scrollregion=self.messageListCanvas.bbox("all"))



	def addNewMessageDialog(self):

		entryBox = Entry()
		entryBox.grid(column=0, row=0, sticky='ew', pady=5)

		addMessage = Button()
		addMessage['text'] = 'Add New Message'
		# addMessage['command'] = main.refreshMessageList
		addMessage.grid(column=1, row=0, sticky='n', padx=10, pady=10)

	def refreshWindow(self):
		logging.debug('Refreshing Message Window')
		self.refreshMessageList()
		self.messageListCanvas.destroy()
		self.vsb.destroy()
		self.hsb.destroy()
		self.createMessageFrame()

		# FIXME Refresh works, we are getting double scroll bars though


if __name__ == "__main__":
	logging.debug("Started main program")
	root = Tk()
	root.columnconfigure(0, weight=1)
	# root.rowconfigure(0, weight=1)
	root.minsize(width=250, height=50)
	root.title('Forge Land Message Editor ' + main.versionNumber)
	root.wm_iconbitmap(bitmap='images/icon.ico')
	main(root).grid()
	root.mainloop()
	logging.debug("EOP")