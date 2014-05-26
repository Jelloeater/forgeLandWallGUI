import json
import logging
import requests as Requests
from settings import settings

__author__ = 'Jesse'

from model import message
import requests


class messageController(message):
	""" Mediates communication and unifies validation, using direct calls """

	@classmethod
	def refreshMessageList(cls):
		""" Gets the messages from the server and loads them into the model """
		numberToGet = cls.numberOfMessagesToGet
		logging.info("Getting " + str(numberToGet) + ' messages from ' + cls.serverAddress)
		rawJSON = Requests.get(settings.serverAddress + 'get/' + str(numberToGet))
		messageList = json.loads(rawJSON.content)

		logging.debug("Got " + str(len(messageList)) + " message(s)")
		message.messageList = messageList
		return messageList  # For testing and other neat things

	@classmethod
	def addMessageToList(cls, messageToAdd):
		""" Adds the messages to server and refreshes list"""
		logging.debug("Adding " + str(messageToAdd))
		data = {'create': messageToAdd}
		requests.post(url=cls.serverAddress+'post', data=data)

	@classmethod
	def editMessage(cls, indexToEdit, newMessage):
		logging.debug('Editing INDEX @: ' + str(indexToEdit) + ' - ' + newMessage)
		data = {'edit': newMessage, 'index': indexToEdit}
		requests.post(url=cls.serverAddress+'post', data=data)

	@classmethod
	def deleteMessage(cls, indexToDelete):
		logging.debug('Deleting INDEX @: ' + str(indexToDelete))
		data = {'delete': indexToDelete}
		requests.post(url=cls.serverAddress+'post', data=data)