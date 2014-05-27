from Tkinter import Tk, Frame, Label, Entry, Button

__author__ = 'Jesse'
import logging
logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", level=logging.DEBUG)

import json
import os

settingsFilePath = "/settings.json"

class settings:
	serverIp = '192.168.1.165'
	port = '9000'
	serverAddress = 'http://' + serverIp + ':' + port + '/'
	numberOfMessagesToGet = 0
	versionNumber = "v1.2"
	defaultMessageBoxText = 'Enter Message / Search'

	@classmethod
	def loadSettings(cls):
		if not os.path.isfile(settingsFilePath):
			logging.warn("Settings missing, defaults set")
		else:
			pass
			# TODO Write JSON based settings load

	@classmethod
	def saveSettings(cls):
		logging.info("Settings saved")
		# TODO Write JSON based settings save


	def editSettings(cls):

		def commitSettings(messageInDialogIn):
			# TODO Get entry and write settings
			messageInDialogIn.destroy()

		messageInDialog = Tk()
		messageInDialog.title('Settings')
		messageInDialog.wm_iconbitmap(bitmap='images/icon.ico')
		messageInDialog.columnconfigure(0, weight=1)
		messageInDialog.rowconfigure(0, weight=1)

		messageInDialog.minsize(width=100, height=50)
		frame = Frame(messageInDialog)

		label = Label(frame)
		label['text'] = 'Server Address'
		label.pack()

		IPAddressBox = Entry(frame)
		IPAddressBox.insert(0, cls.serverIp)
		IPAddressBox.pack(fill='both')

		portLabel = Label(frame)
		portLabel['text'] = 'Server Port'
		portLabel.pack()


		portBox = Entry(frame)
		portBox.insert(0, cls.port)
		portBox.pack(fill='both')

		label['text'] = 'Server Port'
		label.pack()

		submitButton = Button(frame)
		submitButton['text'] = 'Ok'
		submitButton['command'] = lambda: commitSettings(messageInDialog)
		submitButton.pack(side="left", expand="yes", fill="both", padx=5, pady=3)

		cancelButton = Button(frame)
		cancelButton['text'] = 'Cancel'
		cancelButton['command'] = messageInDialog.destroy
		cancelButton.pack(fill='both', expand="yes", padx=5, pady=3)

		frame.pack(fill='both', expand="yes", padx=0, pady=0)