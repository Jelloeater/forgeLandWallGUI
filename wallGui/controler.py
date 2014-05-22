__author__ = 'Jesse'
from settings import *

class messageList(web):
	def getMessagesFromServer(cls,numberToGet):
		rawJson = urllib.urlopen(web.serverAddress+'get/'+str(numberToGet))
		print(rawJson)



