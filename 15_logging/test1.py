
import logging
import student1
logger=logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('test1.log', mode='a')
file_handler.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s', 
datefmt='%d-%m-%Y %I:%M:%S %p')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


logger.debug('DEBUG message from test module')
logger.info('INFO message from test module')
logger.warning('WARNING message from test module')
logger.error('ERROR message from test module')
logger.critical('CRITICAL message from test module')