import Tkinter
import logging

logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", level=logging.DEBUG)

def main():
	logging.debug("Started main program")

main()