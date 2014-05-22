__author__ = 'Jesse'
from settings import webSettings
import requests as Requests
import json
import logging

class message(webSettings):
	""" The Data"""
	messageTable = []
	def __init__(self):
		self.message = None
		self.timestamp = None
		self.index = None

	@classmethod
	def getMessagesFromServer(cls, numberToGet):
		""" Gets the messages from the server and loads them into the model """
		logging.info("Getting " + str(numberToGet) + ' messages from ' + cls.serverAddress)
		rawJSON = Requests.get(webSettings.serverAddress+'get/'+str(numberToGet))
		messageList = json.loads(rawJSON.content)

		logging.debug("Got messages")
		return messageList # For testing and other neat things
		# FIXME Load message list up with data

