from Tkinter import *

class AppUI(Frame,Button):
	labelText = "main Lab"
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

		newlab = Label()
		newlab.labelText = StringVar()
		newlab['textvariable'] = newlab.labelText
		newlab.grid(sticky='nsew')
		newlab.labelText.set("meowwwwwwe34")

		newlab2 = Button()
		newlab2.labelText = StringVar()
		newlab2['textvariable'] = newlab2.labelText
		newlab2.grid(sticky='nsew')
		newlab2.labelText.set("cats22")
		newlab2['command'] = lambda: newlab2.labelText.set(newlab2.labelText.get() + "I'mma cat too")

		newlab3 = Button()
		newlab3.labelText = StringVar()
		newlab3['textvariable'] = newlab3.labelText
		newlab3.grid(sticky='nsew')
		newlab3.labelText.set("cats1232222")
		newlab3['command'] = lambda: newlab3.labelText.set(newlab2.labelText.get() + "I'mma cat too")




		autoRefresh(self)
		# autoRefresh(root)
		# quitButton(root)
		#
		# quitButton(root)
		quitButton(self)

		self.obj = label(self)
		# obj.changeVariable("meowwww")
		self.obj.labelText.set("catsssss")
		# print(obj.labelText.get())



		def sayHi(name):
			print 'hello,', name

		btnaText='ButtonA'
		btna = Button(root, text = btnaText, command = lambda: sayHi(btnaText))
		btnaText = "fuck man"
		btna.grid()





		someButton(self)

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

	@classmethod
	def makeNewWindow(cls):
		root = Tk()
		root.columnconfigure(0, weight=1)
		app = AppUI(root)
		app.grid()


class label(Label):
	def __init__(self, parent):
		Label.__init__(self, parent)
		self.labelText = StringVar()
		self['textvariable'] = self.labelText
		self.grid(sticky='nsew')

	def setText(self, text):
		self.labelText = text


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

class someButton(Button):
	variable = ""
	def __init__(self, parent):
		Button.__init__(self, parent)
		# Change the message here
		self['text'] = label
		# Command to close the window (the destory method)
		# self['command'] = newlab.labelText.set("meowwwwwwe34")
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
		editMenu.add_command(label="Cut", command=AppUI.makeNewWindow)
		editMenu.add_command(label="Copy")
		editMenu.add_command(label="Paste")
		self.master.config(menu=self.menubar)



root = Tk()
root.columnconfigure(0, weight=1)
app = AppUI(root)
app.grid()


root.mainloop()

