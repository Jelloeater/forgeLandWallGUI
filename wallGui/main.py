import Tkinter
import logging
from controler import messageController

class main(messageController):
	@classmethod
	def main(cls):
		logging.debug("Started main program")
		cls.refreshMessageList(2)
		logging.debug("EOP")

main.main()