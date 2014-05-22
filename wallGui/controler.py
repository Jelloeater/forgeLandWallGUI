import json
import logging
import requests as Requests
from settings import webSettings

__author__ = 'Jesse'

from model import message

class messageController(message):
	""" Mediates communication and unifies validation, using direct calls """

	@classmethod
	def refreshMessageList(cls, numberToGet):
		""" Gets the messages from the server and loads them into the model """
		logging.info("Getting " + str(numberToGet) + ' messages from ' + cls.serverAddress)
		rawJSON = Requests.get(webSettings.serverAddress+'get/'+str(numberToGet))
		messageList = json.loads(rawJSON.content)

		logging.debug("Got messages")
		message.messageList = messageList
		return messageList  # For testing and other neat things