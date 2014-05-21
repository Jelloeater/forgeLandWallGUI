__author__ = 'Jesse'


class messageList(web):
	def getMessagesFromServer(cls,numberToGet):
		rawJson = urllib.urlopen(web.serverAddress+'get/'+str(numberToGet))
		print(rawJson)
from settings import *

__author__ = 'Jesse'
