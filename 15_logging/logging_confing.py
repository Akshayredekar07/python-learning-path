
import logging
import logging.config

# logging.config.fileConfig("logging_config.ini")
logging.config.fileConfig("logging_config_console_handler.ini")
logger = logging.getLogger('demologger')
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')
