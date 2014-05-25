from Tkinter import *
import logging
from controler import messageController

class main(Frame, messageController):
	def __init__(self, rootWindow):
		Frame.__init__(self, root)
		menuBar(root)

		self.refreshMessageList()

		self.topFrame = Frame()
		entryBox = Entry(self.topFrame)
		entryBox.pack(side='left', fill='x', expand='True')


		addMessage = Button(self.topFrame)
		addMessage['text'] = 'Add New Message'
		# addMessage['command'] = main.refreshMessageList
		addMessage.pack(side='right', padx=10)
		self.topFrame.pack(fill='x')


		self.canvas = Canvas(root, borderwidth=0)
		self.frame = Frame(self.canvas)
		self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.vsb.pack(side="right", fill="y")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
		self.frame.bind("<Configure>", self.OnFrameConfigure)

		self.messageListBox()


	def messageListBox(self):
		messagesToLoad = self.messageList # Fetch Message List from model

		# FIXME Get button instances
		# http://tkinter.unpythonic.net/wiki/CallbackConfusion
		# http://stackoverflow.com/questions/728356/dynamically-creating-a-menu-in-tkinter-lambda-expressions
		for i in messagesToLoad:
			rowToInsertAt = messagesToLoad.index(i) + 1

			messageText = Label(self.frame)
			messageText['text'] = i
			messageText.grid(column=0, row=rowToInsertAt, sticky='w', padx=10)

			editButton = Button(self.frame)
			editButton['text'] = 'Edit'
			# editButton['command'] = lambda rowToInsertAt=rowToInsertAt: self.editMessage(messagesToLoad[rowToInsertAt-1])
			editButton['command'] = lambda i=i: self.editMessage(i)
			editButton.grid(column=1, row=rowToInsertAt, sticky='e')

			deleteButton = Button(self.frame)
			deleteButton['text'] = 'Delete'
			deleteButton['command'] = lambda i=i: self.deleteMessage(i)
			deleteButton.grid(column=2, row=rowToInsertAt, sticky='e', padx=10)
			logging.debug(i)
			logging.debug(rowToInsertAt)


	def editMessage(self, c):
		logging.debug('Editing: ' + str(c))
		# TODO Write Edit function

	def deleteMessage(self,c):
		logging.debug('Deleting: ' + str(c))
		# TODO Write Delete Function


	def OnFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))



	def addNewMessageDialog(self):

		entryBox = Entry()
		entryBox.grid(column=0, row=0, sticky='ew', pady=5)

		addMessage = Button()
		addMessage['text'] = 'Add New Message'
		# addMessage['command'] = main.refreshMessageList
		addMessage.grid(column=1, row=0, sticky='n', padx=10, pady=10)

class menuBar(Menu):
	def __init__(self, parent, **kw):
		Menu.__init__(self, parent)
		self.menubar = Menu()
		fileMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=fileMenu, underline=1)
		fileMenu.add_command(label="Quit", command=parent.destroy, underline=1)
		optionsMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Options", menu=optionsMenu)
		optionsMenu.add_command(label="Refresh", command=main.refreshMessageList, underline=1)
		optionsMenu.add_command(label="Server Settings")
		editMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=editMenu)
		editMenu.add_command(label="Help")
		editMenu.add_command(label="About")
		self.master.config(menu=self.menubar)


if __name__ == "__main__":
	logging.debug("Started main program")
	root = Tk()
	root.columnconfigure(0, weight=1)
	# root.rowconfigure(0, weight=1)
	root.minsize(width=400, height=50)
	root.title('Forge Land Message Editor ' + main.versionNumber)
	root.wm_iconbitmap(bitmap='images/icon.ico')
	main(root).grid()
	root.mainloop()
	logging.debug("EOP")