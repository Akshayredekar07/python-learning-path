
import logging  
import os  
from datetime import datetime 


# Creates a log file name with current timestamp in format MM_DD_YYYY_HH_MM_SS.log
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Generates timestamp (e.g., "08_06_2025_13_11_23.log" for 01:11:23 PM IST on 08/06/2025)
# Variable: LOG_FILE
#   - Purpose: Stores the name of the log file with a timestamp
#   - Type: str (e.g., "08_06_2025_13_11_23.log")

# Creates path for logs directory by joining current working directory with "logs"
log_path=os.path.join(os.getcwd(),"logs")
# Joins current directory (e.g., "D:\Langchain") with "logs" (e.g., "D:\Langchain\logs")
# Variable: log_path
#   - Purpose: Stores the path to the logs directory
#   - Type: str (e.g., "D:\Langchain\logs")

# Creates logs directory if it doesn't exist
os.makedirs(log_path,exist_ok=True)
# Ensures "D:\Langchain\logs" exists; creates it if missing, does nothing if already present
# Method: os.makedirs
#   - Purpose: Creates a directory (and parent directories if needed)
#   - Return Type: None

# Combines logs directory path with log file name
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)
# Joins "D:\Langchain\logs" with "08_06_2025_13_11_23.log" (e.g., "D:\Langchain\logs\08_06_2025_13_11_23.log")
# Variable: LOG_FILEPATH
#   - Purpose: Stores the full path to the log file
#   - Type: str (e.g., "D:\Langchain\logs\08_06_2025_13_11_23.log")

# Configures logging with INFO level, file output, and custom format
logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
# Sets up logging to write INFO-level (and above) messages to the log file with format
# Method: logging.basicConfig
#   - Purpose: Configures the root logger with specified level, file, and format
#   - Return Type: None
# Log format example: "[2025-08-06 13:11:23,456] 6 root - INFO - this my second tesgting"