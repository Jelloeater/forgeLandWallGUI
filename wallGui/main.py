from Tkinter import *
import logging
from controler import messageController

class main(messageController):
	@classmethod
	def main(cls):
		logging.debug("Started main program")
		cls.refreshMessageList()
		root = Tk()
		root.columnconfigure(0, weight=1)
		# root.rowconfigure(0, weight=1)
		root.minsize(width=400, height=50)
		root.title('Forge Land Message Editor ' + cls.versionNumber)
		root.wm_iconbitmap(bitmap='images/icon.ico')

		menuBar(root)

		addNewMessageDialog(root)

		messageList(root)


		# root.grid()
		root.mainloop()

		logging.debug("EOP")

class addNewMessageDialog(Frame, main):
	def __init__(self, parent, **kw):
		Frame.__init__(self, parent, **kw)

		entryBox = Entry()
		entryBox.grid(column=0, row=0, sticky='ew', pady=5)

		addMessage = Button(parent)
		addMessage['text'] = 'Add New Message'
		# addMessage['command'] = main.refreshMessageList
		addMessage.grid(column=1, row=0, sticky='', padx=10, pady=5)


class messageList(Frame, main):
	def __init__(self, parent, **kw):
		Frame.__init__(self, parent, **kw)

		messagesToLoad = ["1", "2", "3"]

		for i in messagesToLoad:
			messageItem(parent, messageIn=i)



class messageItem(Frame, main):
	def __init__(self, parent, messageIn, **kw):
		Frame.__init__(self, parent, **kw)
		messageText = Label()
		messageText['text'] = messageIn
		messageText.grid(column=0, sticky='n')

		editButton = Button()
		editButton['text'] = 'Edit'
		editButton.grid(column=1, sticky='n')

		deleteButton = Button()
		deleteButton['text'] = 'Delete'
		deleteButton.grid(column=2, sticky='n')


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


main.main()