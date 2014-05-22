__author__ = 'Jesse'

from model import message

class messageController(message):
	""" Mediates communication and unifies validation, using direct calls """
	@classmethod
	def loadMessages(cls,numberToGet):
		""" Calls the message table population method"""
		message.getMessagesFromServer()



