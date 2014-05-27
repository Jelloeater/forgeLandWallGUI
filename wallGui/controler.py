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

		if settings.isServerActive():
			numberToGet = cls.numberOfMessagesToGet
			logging.info("Getting " + str(numberToGet) + ' messages from ' + 'http://' + cls.serverIp + ':' + cls.port + '/')
			rawJSON = Requests.get(cls.getServerAddress() + 'get/' + str(numberToGet))
			messageList = json.loads(rawJSON.content)

			logging.debug("Got " + str(len(messageList)) + " message(s)")
			message.messageList = messageList
			return messageList  # For testing and other neat things
		else:
			return False

	@classmethod
	def addMessageToList(cls, messageToAdd):
		""" Adds the messages to server """
		if cls.isServerActive():
			if messageToAdd != cls.defaultMessageBoxText and not str(messageToAdd).isspace():
				logging.debug("Adding " + str(messageToAdd))
				data = {'create': messageToAdd}
				requests.post(url=cls.getServerAddress() + 'post', data=data)
				return True
			else:
				logging.warning('User did not enter a non default message')
				return False

	@classmethod
	def editMessage(cls, indexToEdit, newMessage):
		""" Edits message via index"""
		if newMessage != '' and newMessage is not None and not str(newMessage).isspace():
			logging.debug('Editing INDEX @: ' + str(indexToEdit) + ' - ' + str(newMessage))
			data = {'edit': newMessage, 'index': indexToEdit}
			requests.post(url=cls.getServerAddress() + 'post', data=data)
			return True
		else:
			logging.warning('User entered a blank message')
			return False

	@classmethod
	def deleteMessage(cls, indexToDelete):
		""" Deletes message from server """
		logging.debug('Deleting INDEX @: ' + str(indexToDelete))
		data = {'delete': indexToDelete}
		requests.post(url=cls.getServerAddress() + 'post', data=data)

	@classmethod
	def searchMessage(cls, messageToSearchFor):
		""" Search for message and return query """
		if messageToSearchFor != '' and messageToSearchFor is not None and not str(messageToSearchFor).isspace():
			logging.debug('Searching for: ' + messageToSearchFor)

			rawJSON = Requests.get(cls.getServerAddress() + 'query/' + str(messageToSearchFor))
			messageList = json.loads(rawJSON.content)
			logging.debug("Got " + str(len(messageList)) + " message(s)")
			message.messageList = messageList
			return messageList  # For testing and other neat things
		else:
			cls.refreshMessageList()
			logging.warning('User entered a blank search')
			return False