
import inspect
def get_info():
    print(inspect.stack())
    print("*"*50,"\n")
    print(inspect.stack()[1])
    print("*"*50, "\n")
    print(f"Caller module name: {inspect.stack()[1][1]}")


 
