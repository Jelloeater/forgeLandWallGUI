from sys import version_info

try:
	from tkinter import *
except ImportError:
	from Tkinter import *

def Pressed():                          #function
	print ('buttons are cool')
	print(v.get())
	if v.get():
		print("cat")
		newWindow = Tk()
		l = Label(newWindow,text="LOL")
		l.pack()
		list = Listbox(newWindow)
		stuff=[1,2]
		for x in stuff:
			list.insert(0,x)
		list.pack()

root = Tk()                             #main window

v = IntVar()
c = Checkbutton(root, text="Don't show this again", variable=v)

c.pack()

button = Button(root, command = Pressed)
button.pack()

root.mainloop()


# https://wiki.python.org/moin/Intro%20to%20programming%20with%20Python%20and%20Tkinter