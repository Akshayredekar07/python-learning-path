

import logging
import logging.config
import json

with open('logging_config.json', 'r') as f:
    config = json.load(f)

logging.config.dictConfig(config)
logger = logging.getLogger('demologger')
logger.critical('It is critical message (JSON)')
logger.error('It is error message (JSON)')
logger.warning('It is warning message (JSON)')
logger.info('It is info message (JSON)')
logger.debug('It is debug message (JSON)')