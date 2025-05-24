

import logging
from logging.config import dictConfig

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format': '%(asctime)s:%(name)s:%(levelname)s:%(message)s',
              'datefmt': '%d/%m/%Y %I:%M:%S %p'}
    },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
    },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)

logger = logging.getLogger()
logger.critical('it is critical message')
logger.error('it is error message')
logger.warning('it is warning message')
logger.info('it is info message')
logger.debug('it is debug message')