
import logging
import inspect

def get_custom_logger(level):
    function_name = inspect.stack()[1][3]  # Get the calling function's name
    logger_name = function_name + " logger"  # Create a unique logger name
    logger = logging.getLogger(logger_name)  # Initialize logger
    logger.setLevel(level)  # Set logger's minimum log level

    fileHandler = logging.FileHandler('{}.log'.format(function_name), mode='a')  # Dynamic file name
    fileHandler.setLevel(level)  # Set handler's log level
    formatter = logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p')  # Define log format
    fileHandler.setFormatter(formatter)  # Apply formatter
    logger.addHandler(fileHandler)  # Add handler to logger
    return logger  # Return configured logger