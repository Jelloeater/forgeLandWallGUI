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