from Tkinter import *

def Pressed():                          #function
	print 'buttons are cool'
	print(v.get())
	if v.get():
		print("cat")

root = Tk()                             #main window

v = IntVar()
c = Checkbutton(root, text="Don't show this again", variable=v)

c.pack()

button = Button(root, command = Pressed)
button.pack()

root.mainloop()

# https://wiki.python.org/moin/Intro%20to%20programming%20with%20Python%20and%20Tkinter