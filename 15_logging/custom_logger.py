
import logging

# Customized logger creation and usage:

# Logger object 
logger = logging.getLogger("demologger")
logger.setLevel(logging.DEBUG)

# Handler object 
# there are mutiple types of handler like StreamHandler, FileHandler etc
# consoleHandler=logging.StreamHandler()
# consoleHandler.setLevel(logging.ERROR)    
fileHandler=logging.FileHandler('abc.log', mode='a')
fileHandler.setLevel(logging.ERROR)

# Formatter object
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s', datefmt="%d-%m-%Y %I:%M:%S %p")


# Add formatter to handler 
# consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# Add handler to logger 
# logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


# Write message by using logger object 
logger.debug("debug msg")
logger.info("info msg")
logger.warning("warning msg")
logger.error("error msg")
logger.critical("critical msg")


# Bydefault the logger level will be 