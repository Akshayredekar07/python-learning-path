
from custlogger import get_custom_logger
import logging

def logtest():
    logger = get_custom_logger(logging.DEBUG)  # Get logger with DEBUG level
    logger.critical('critical message from test module')
    logger.error('error message from test module')
    logger.warning('warning message from test module')
    logger.info('info message from test module')
    logger.debug('debug message from test module')

logtest()