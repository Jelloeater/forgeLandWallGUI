from Tkinter import Tk, Frame, Label, Entry, Button
import tkMessageBox
from urllib2 import urlopen, URLError
import json
import os

__author__ = 'Jesse'
import logging
import os
logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", level=logging.DEBUG)

settingsFilePath = "settings.json"


class settingsVars:
	serverIp = '192.168.1.165'
	port = '9000'
	numberOfMessagesToGet = 0
	versionNumber = "v1.65"
	defaultMessageBoxText = 'Enter Message / Search'
	refreshInterval = 5


class settings(settingsVars):

	@classmethod
	def getDict(cls, obj):
		"""The default encoder to take the object instances	fields as JSON fields"""
		return obj.__dict__

	@classmethod
	def getServerAddress(cls):
		return 'http://' + settings.serverIp + ':' + settings.port + '/'


	@classmethod
	def isServerActive(cls):
		logging.debug('Checking server')
		try:
			urlopen(cls.getServerAddress(), timeout=1)
			return True
		except URLError:
			logging.warning('Cannot Reach Server @ ' + cls.getServerAddress())
			return False


	@classmethod
	def loadSettings(cls):
		if os.path.isfile(settingsFilePath):
			fh = open(settingsFilePath, mode='r')
			settingsVars.__dict__ = json.loads(fh.read())
			fh.close()
			logging.info("Settings loaded")
		else:
			logging.warn("Settings missing, defaults set")


	@classmethod
	def saveSettings(cls):
		fh = open(settingsFilePath, mode='w')
		fh.write(json.dumps(settingsVars.__dict__, sort_keys=True, indent=0))
		fh.close()
		logging.info("Settings saved")


	@classmethod
	def editSettings(cls):

		def commitSettings(messageInDialogIn):
			# Temp vars
			ip = settings.serverIp
			p = settings.port

			settingsVars.serverIp = IPAddressBox.get()
			settingsVars.port = portBox.get()
			settingsVars.numberOfMessagesToGet = int(numberToGetBox.get())
			settingsVars.refreshInterval = int(refreshIntervalBox.get())

			if not cls.isServerActive():
				settingsVars.serverIp = ip
				settingsVars.port = p
				tkMessageBox.showerror(message='Invalid Server Address ' + 'http://' + IPAddressBox.get() + ':' + portBox.get() + '/')
				logging.warning('Invalid Server Address ' + 'http://' + IPAddressBox.get() + ':' + portBox.get() + '/')
			messageInDialogIn.destroy()

		settingsDialog = Tk()
		settingsDialog.title('Settings')
		if os.name == "nt":
			settingsDialog.wm_iconbitmap(bitmap='images/icon.ico')
		settingsDialog.columnconfigure(0, weight=1)
		settingsDialog.rowconfigure(0, weight=1)

		settingsDialog.minsize(width=100, height=50)
		frame = Frame(settingsDialog)

		addressLabel = Label(frame)
		addressLabel['text'] = 'Server Address'
		addressLabel.pack()

		IPAddressBox = Entry(frame)
		IPAddressBox.insert(0, cls.serverIp)
		IPAddressBox.pack(fill='both')

		portLabel = Label(frame)
		portLabel['text'] = 'Server Port'
		portLabel.pack()

		portBox = Entry(frame)
		portBox.insert(0, cls.port)
		portBox.pack(fill='both')

		numberToGetLabel = Label(frame)
		numberToGetLabel['text'] = '# of Messages To Get'
		numberToGetLabel.pack()

		numberToGetBox = Entry(frame)
		numberToGetBox.insert(0, cls.numberOfMessagesToGet)
		numberToGetBox.pack(fill='both')

		refreshIntervalLabel = Label(frame)
		refreshIntervalLabel['text'] = 'Refresh Interval'
		refreshIntervalLabel.pack()

		refreshIntervalBox = Entry(frame)
		refreshIntervalBox.insert(0, cls.refreshInterval)
		refreshIntervalBox.pack(fill='both')

		submitButton = Button(frame)
		submitButton['text'] = 'Ok'
		submitButton['command'] = lambda: commitSettings(settingsDialog)
		submitButton.pack(side="left", expand="yes", fill="both", padx=5, pady=3)

		cancelButton = Button(frame)
		cancelButton['text'] = 'Cancel'
		cancelButton['command'] = settingsDialog.destroy
		cancelButton.pack(fill='both', expand="yes", padx=5, pady=3)

		frame.pack(fill='both', expand="yes", padx=0, pady=0)

		return settingsDialog
