import sys  

class CustomError(Exception):
    def __init__(self, error_message, error_details):
        # When an instance of CustomError is created, this method runs
        # 1. Stores the error message (e.g., "division by zero") in self.error_message
        # 2. Calls sys.exc_info() to get error details
        # 3. Extracts line number and file name from the traceback
        # Variable: error_message
        #   - Purpose: Stores the error message from the original exception
        #   - Type: Any (usually a string or Exception object)
        # Variable: error_details
        #   - Purpose: Refers to the sys module to access error information
        #   - Type: Module (sys module)
        # Variable: self.error_message
        #   - Purpose: Instance variable to hold the error message
        #   - Type: Any (usually a string or Exception object)
        # Variable: self.line_number
        #   - Purpose: Stores the line number where the error occurred
        #   - Type: int
        # Variable: self.file_name
        #   - Purpose: Stores the name of the file where the error occurred
        #   - Type: str
        # Return Type: None (constructor initializes the object)
        
        self.error_message = error_message  # Stores the original error message
        
        # Get error details: sys.exc_info() returns a tuple (type, value, traceback)
        _, _, error_traceback = error_details.exc_info()
        # Variable: error_traceback
        #   - Purpose: Holds the traceback object containing error location details
        #   - Type: traceback object
        
        # Get the line number where the error occurred
        self.line_number = error_traceback.tb_lineno  # Sets line number (e.g., 26)
        
        # Get the file name where the error occurred
        self.file_name = error_traceback.tb_frame.f_code.co_filename  # Sets file name (e.g., "error_script.py")
    
    def __str__(self):
        # Called when the error is printed or raised
        # 1. Returns a formatted string with file name, line number, and error message
        # Method: __str__
        #   - Purpose: Defines how the CustomError object is represented as a string
        #   - Return Type: str
        return f"Error in script '{self.file_name}' at line {self.line_number}: {self.error_message}"  # Returns formatted string, e.g., "Error in script 'error_script.py' at line 26: division by zero"



if __name__ == "__main__":
    # This block runs when the script is executed directly
    try:
        # Attempts to execute the code inside
        # 1. Tries to divide 1 by 0, which raises a ZeroDivisionError
        # Variable: result
        #   - Purpose: Stores the result of the division (never assigned due to error)
        #   - Type: Would be float, but error occurs
        result = 1 / 0  # Raises ZeroDivisionError, jumps to except block
    except Exception as error:
        # Catches the ZeroDivisionError
        # 1. The error is stored in the variable 'error'
        # 2. Raises a CustomError with the original error and sys module
        # Variable: error
        #   - Purpose: Holds the caught exception (e.g., ZeroDivisionError)
        #   - Type: Exception object
        raise CustomError(error, sys)
        # Creates and raises CustomError
        # 1. CustomError.__init__ is called with error="division by zero" and sys module
        # 2. sys.exc_info() extracts traceback details
        # 3. Line number (e.g., 26) and file name (e.g., "error_script.py") are stored
        # 4. CustomError.__str__ is called, producing a formatted error message
        # 5. Python prints the traceback and the custom error message