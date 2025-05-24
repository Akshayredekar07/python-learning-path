
import logging
import logging.config
import yaml

with open('logging_confing.yaml', 'r') as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)
logger = logging.getLogger('demologger')
logger.critical('It is critical message (YAML)')
logger.error('It is error message (YAML)')
logger.warning('It is warning message (YAML)')
logger.info('It is info message (YAML)')
logger.debug('It is debug message (YAML)')