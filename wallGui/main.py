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
		root.rowconfigure(0, weight=1)
		root.minsize(width=400, height=50)
		root.title('Forge Land Message Editor ' + cls.versionNumber)
		root.wm_iconbitmap(bitmap='images/icon.ico')

		menuBar(root)
		newMessageBox(root)
		addMessage(root)





		root.grid()
		root.mainloop()

		logging.debug("EOP")


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


class addMessage(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		self['text'] = 'Add Message'
		# self['command'] = main.refreshMessageList
		# self['accelerator'] = "F5"
		self.grid(column=1, row=0, sticky='', padx=10, pady=5)


class newMessageBox(Entry):
	def __init__(self, parent, **kw):
		Entry.__init__(self, **kw)
		self.grid(column=0, row=0, sticky='ew', padx=10, pady=5)

main.main()