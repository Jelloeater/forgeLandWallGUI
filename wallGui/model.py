__author__ = 'Jesse'
from settings import webSettings
import requests as Requests
import json


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
		rawJSON = Requests.get(webSettings.serverAddress+'get/'+str(numberToGet))
		messageList = json.loads(rawJSON)

