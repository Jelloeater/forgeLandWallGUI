from Tkinter import Tk, Frame, Label, Entry, Button
from urllib2 import urlopen, URLError
# import json
import os

__author__ = 'Jesse'
import logging
logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", level=logging.DEBUG)

settingsFilePath = "/settings.json"


class settings:
	serverIp = '192.168.1.160'
	port = '9000'
	numberOfMessagesToGet = 0
	versionNumber = "v1.5"
	defaultMessageBoxText = 'Enter Message / Search'

	@staticmethod
	def isServerActive():
		logging.debug('Checking server')
		try:
			urlopen('http://' + settings.serverIp + ':' + settings.port + '/', timeout=1)
			return True
		except URLError:
			logging.warning('Cannot Reach Server @ ' + 'http://' + settings.serverIp + ':' + settings.port + '/')
			return False

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

	@classmethod
	def editSettings(cls, startup=False):

		def commitSettings(messageInDialogIn):
			# Temp vars
			ip = settings.serverIp
			p = settings.port

			settings.serverIp = IPAddressBox.get()
			settings.port = portBox.get()
			logging.critical(IPAddressBox.get())

			logging.critical('NewIP' + settings.serverIp)
			logging.critical('New Address' + 'http://' + settings.serverIp + ':' + settings.port + '/')

			if not cls.isServerActive():
				settings.serverIp = ip
				settings.port = p
				logging.warning('Invalid Server Address ' + 'http://' + cls.serverIp + ':' + cls.port + '/')
			else:
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

		if startup:messageInDialog.mainloop()