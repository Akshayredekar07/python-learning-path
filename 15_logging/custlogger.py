
import logging
import inspect

def get_custom_logger(level):
    function_name = inspect.stack()[1][3]  # Get the name of the calling function
    logger_name = function_name + " logger"  # Create a unique logger name
    logger = logging.getLogger(logger_name)  # Initialize logger with the name
    logger.setLevel(level)  # Set the logger's minimum log level

    fileHandler = logging.FileHandler('abc.log', mode='a')  # Append to abc.log
    fileHandler.setLevel(level)  # Set handler's log level
    formatter = logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p')  # Define log format
    fileHandler.setFormatter(formatter)  # Apply formatter to handler
    logger.addHandler(fileHandler)  # Add handler to logger
    return logger  # Return the configured logger