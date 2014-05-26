__author__ = 'Jesse'
import logging
logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", level=logging.DEBUG)


class settings:
	serverIp = '192.168.1.165'
	port = '9000'
	serverAddress = 'http://'+ serverIp + ':'+ port + '/'
	numberOfMessagesToGet = 15
	versionNumber = "v1.0"
	# TODO Write JSON based settings save and load