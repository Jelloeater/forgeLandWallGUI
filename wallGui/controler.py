import json
import logging
import requests as Requests
from settings import webSettings

__author__ = 'Jesse'

from model import message

class messageController(message):
	""" Mediates communication and unifies validation, using direct calls """

	@classmethod
	def refreshMessageList(cls):
		""" Gets the messages from the server and loads them into the model """
		numberToGet = cls.numberOfMessagesToGet
		logging.info("Getting " + str(numberToGet) + ' messages from ' + cls.serverAddress)
		rawJSON = Requests.get(webSettings.serverAddress+'get/'+str(numberToGet))
		messageList = json.loads(rawJSON.content)

		logging.debug("Got messages")
		message.messageList = messageList
		return messageList  # For testing and other neat things

	@classmethod
	def addMessageToList(cls, messageToAdd):
		""" Adds the messages to server and refreshes list"""
		logging.info("Adding " + str(messageToAdd))
		# TODO Add message via POST

		cls.refreshMessageList()
		logging.debug("Added messages")