import logging 
import sys

def main():
    logger = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    logger.info("Initializing Argus Automation Service...")
    logger.info("Argus Automation Service online.")

if __name__ == "__main__": 
    main()