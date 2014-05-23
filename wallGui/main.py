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

		menuBar(root)
		refreshList(root)





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
		editMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=editMenu)
		editMenu.add_command(label="About")
		self.master.config(menu=self.menubar)

class refreshList(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		self['text'] = 'Refresh List (F5)'
		self['command'] = main.refreshMessageList
		# self['accelerator'] = "F5"
		self.grid(sticky='nsew')

main.main()