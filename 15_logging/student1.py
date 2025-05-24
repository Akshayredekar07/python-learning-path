

import logging
logger=logging.getLogger('student_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('student1.log', mode='w')
file_handler.setLevel(logging.ERROR)

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s', 
datefmt='%d-%m-%Y %I:%M:%S %p')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


logger.debug('DEBUG message from student module')
logger.info('INFO message from student module')
logger.warning('WARNING message from student module')
logger.error('ERROR message from student module')
logger.critical('CRITICAL message from student module')


