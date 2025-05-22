import logging 
import sys

def main():
    logger = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    logger.info("Initializing Argus Robotic Client...")

    # initialization

    # start REPL for operator input

    logger.info("Argus Robotic Client online.")

if __name__ == "__main__": 
    main()