import logging

# Logger object
logger = logging.getLogger("demologger")
logger.setLevel(logging.DEBUG)

# Handler objects
# Console handler for output to terminal
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)  # Console logs ERROR and above

# File handler for output to file
fileHandler = logging.FileHandler('abc.log', mode='a')  # Append mode
fileHandler.setLevel(logging.ERROR)  # File logs ERROR and above

# Formatter object
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p")

# Add formatter to handlers
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# Log messages
logger.debug("debug msg")    # Won't appear (below ERROR level)
logger.info("info msg")      # Won't appear (below ERROR level)
logger.warning("warning msg") # Won't appear (below ERROR level)
logger.error("error msg")    # Will appear in both console and file
logger.critical("critical msg")  # Will appear in both console and file