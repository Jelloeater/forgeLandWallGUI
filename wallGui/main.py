from Tkinter import *

class AppUI(Frame):
	def button(self):
		btn = Button()
		self.labelText = StringVar()
		btn['textvariable'] = self.labelText
		btn.grid(sticky='nsew')
		self.labelText.set("cats22")
		btn['command'] = lambda: self.labelText.set(self.labelText.get() + "I'mma cat too")
		return self

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

		messageList = Frame(root)
		msgScrollbar = Scrollbar(messageList)

		newlist = Listbox(messageList)
		stuff = ['cat']
		newlist.insert(0,stuff)
		newlist.grid(row= 0, column=0)


		msgScrollbar.grid(row=0, column=1, sticky=NS)
		messageList.grid(row=0, column=0)


		newlab = Label()
		newlab.labelText = StringVar()
		newlab['textvariable'] = newlab.labelText
		newlab.grid(sticky='nsew')
		newlab.labelText.set("meowwwwwwe34")

		button1 = self.button()
		button1.labelText.set("cattbutton")

		newlab3 = Button()
		newlab3.labelText = StringVar()
		newlab3['textvariable'] = newlab3.labelText
		newlab3.grid(sticky='nsew')
		newlab3.labelText.set("cats1232222")
		# newlab3['command'] = lambda: newlab3.labelText.set(button1.labelText.get() + "I'mma cat too")
		# newlab3['command'] = lambda: newlab3.labelText.set(button1.)




		autoRefresh(self)
		# autoRefresh(root)
		# quitButton(root)
		#
		# quitButton(root)
		quitter = quitButton(self)
		quitter.labelText.set("not a quitter")
		print(quitter.labelText.get())

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


class autoRefresh(Checkbutton):
	def __init__(self, parent):
		Checkbutton.__init__(self, parent)
		self['text'] = 'Refresh'
		self.grid()


class quitButton(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		# Change the message here
		self.labelText = StringVar()
		self['textvariable'] = self.labelText
		self.labelText.set("catquitter")
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
		self.menubar.add_cascade(label="Help", menu=editMenu)
		editMenu.add_command(label="About", command=AppUI.makeNewWindow)
		self.master.config(menu=self.menubar)



root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight = 1)
app = AppUI(root)
app.grid()

app.mainloop()

