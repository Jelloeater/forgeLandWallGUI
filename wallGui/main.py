import Tkinter
import logging
from controler import messageController

logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", level=logging.DEBUG)
class main(messageController):
	@classmethod
	def main(cls):
		logging.debug("Started main program")

main.main()