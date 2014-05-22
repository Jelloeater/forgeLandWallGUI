__author__ = 'Jesse'
from settings import webSettings


class message(webSettings):
	""" The Data"""
	messageTable = []
	def __init__(self):
		self.message = None
		self.timestamp = None
		self.index = None

	@classmethod
	def getMessagesFromServer(cls):
		""" Gets the messages from the server and loads them into the model """
		pass

