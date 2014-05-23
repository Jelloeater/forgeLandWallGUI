from Tkinter import *
import logging
from controler import messageController

class menuBar(Menu):
	def __init__(self, parent, **kw):
		Menu.__init__(self, **kw)
		self.menubar = Menu()
		fileMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=fileMenu)
		fileMenu.add_command(label="Quit", command = parent.destroy)
		editMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=editMenu)
		editMenu.add_command(label="About")
		self.master.config(menu=self.menubar)

class main(messageController):	
	@classmethod
	def main(cls):
		logging.debug("Started main program")
		cls.refreshMessageList()
		root = Tk()
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)

		menuBar(root)

		root.grid()
		root.mainloop()

		logging.debug("EOP")



main.main()