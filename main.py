from Tkinter import *

class AppUI(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master, bd=2)

		# self.menuBar()
		menuBar(root)


		# self.v = IntVar()
		# c = Checkbutton(root, text="Don't show this again", variable=self.v)
		#
		# c.grid(column=0, sticky='WE')
		#
		# button = Button(root, text = 'Press Me', command = self.Pressed)
		# button.grid(column=2, sticky='WE')
		autoRefresh(self)
		quitButton(root)

		quitButton(root)
		quitButton(self)
		quitButton(self)

		# def Pressed(self):                          #function
		# 	print 'buttons are cool'
		# 	print(self.v.get())
		# 	if self.v.get():
		# 		print("cat")
		# 		new = Tk()
		# 		box = Canvas(new)
		# 		box.grid()
	@classmethod
	def Exit(cls):
		root.destroy()

class autoRefresh(Checkbutton):
	def __init__(self, parent):
		Checkbutton.__init__(self, parent)
		self['text'] = 'Refresh'
		self.grid()


class quitButton(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		# Change the message here
		self['text'] = 'Good Bye'
		# Command to close the window (the destory method)
		self['command'] = root.destroy
		self.grid(sticky='nsew')

# Create a class that specializing the Button class from the tkinter
class menuBar(Menu):
	def __init__(self, parent, **kw):
		Menu.__init__(self, **kw)
		self.menubar = Menu()
		fileMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=fileMenu)
		fileMenu.add_command(label="Quit", command=AppUI.Exit)
		editMenu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Edit", menu=editMenu)
		editMenu.add_command(label="Cut")
		editMenu.add_command(label="Copy")
		editMenu.add_command(label="Paste")
		self.master.config(menu=self.menubar)



root = Tk()
root.columnconfigure(0, weight=1)
app = AppUI(root)
app.grid()

root.mainloop()

