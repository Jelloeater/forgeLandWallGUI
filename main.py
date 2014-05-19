from Tkinter import *


class AppUI(Frame):

	def menuBar(self):
		self.menubar = Menu(self)
		menu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=menu)
		menu.add_command(label="Quit", command=self.Exit)
		menu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Edit", menu=menu)
		menu.add_command(label="Cut")
		menu.add_command(label="Copy")
		menu.add_command(label="Paste")
		self.master.config(menu=self.menubar)


	def Exit(self):
		root.destroy()


	def __init__(self, master=None):
		Frame.__init__(self, master, bd=2)

		self.menuBar()

		# self.v = IntVar()
		# c = Checkbutton(root, text="Don't show this again", variable=self.v)
		#
		# c.grid(column=0, sticky='WE')
		#
		# button = Button(root, text = 'Press Me', command = self.Pressed)
		# button.grid(column=2, sticky='WE')
		quitButton(root)
		quitButton(self)

	# def Pressed(self):                          #function
	# 	print 'buttons are cool'
	# 	print(self.v.get())
	# 	if self.v.get():
	# 		print("cat")
	# 		new = Tk()
	# 		box = Canvas(new)
	# 		box.grid()


# Create a class that specializing the Button class from the tkinter
class quitButton(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		# Change the message here
		self['text'] = 'Good Bye'
		# Command to close the window (the destory method)
		self['command'] = parent.destroy
		self.grid(row=1,sticky='nsew')


root = Tk()
root.columnconfigure(0, weight=1)
app = AppUI(root)
app.grid()

root.mainloop()

