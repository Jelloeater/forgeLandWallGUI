import json
import logging
import requests as Requests
from settings import settings
from model import message
import requests
import threading

__author__ = 'Jesse'


class messageController(message):
	""" Mediates communication and unifies validation, using direct calls """
	autoRefreshLock = threading.Lock()  # Refresh lock object used to mediate application

	@classmethod
	def refreshMessageList(cls):
		""" Gets the messages from the server and loads them into the model """

		if settings.isServerActive():
			numberToGet = cls.numberOfMessagesToGet

			rawJSON = Requests.get(cls.getServerAddress() + 'get/' + str(numberToGet))
			messageList = json.loads(rawJSON.content)

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
		""" Search for message and return query, only takes valid messages """
		logging.debug('*REFRESH LOCK STATUS* = ' + str(cls.autoRefreshLock.locked()))
		logging.debug('Searching for: ' + messageToSearchFor)

		searchGetObj = Requests.get(cls.getServerAddress() + 'query/' + str(messageToSearchFor))
		if searchGetObj.content != ']':
			logging.debug(searchGetObj.content)
			messageList = json.loads(searchGetObj.content)
			logging.debug("Got " + str(len(messageList)) + " message(s)")
			message.messageList = messageList
			return messageList  # For testing and other neat things
		else:
			# Does not set json return to model messageList data (we ignore bad input due to not finding any results)
			logging.info('No Results Found')
			return False
