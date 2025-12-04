def debug(func):
    def wrapper(*args , **kwargs):
        args_value =', '.join(str(arg) for arg in args) # Convert args tuple to a string
        kwargs_value ='. '.join( f"{k}:{v}" for k,v in kwargs.items()) # Convert kwargs dict to a string
        function_name = func.__name__ # Get the name of the function being decorated
        print(f"Calling {function_name} with arguments: {args_value} and keyword arguments: {kwargs_value}")
        return func(*args , **kwargs) # Call the original function
    return wrapper





@debug   # Decorate the greet function with the debug decorator
def greet(name, greeting = "Hello"):
    print (f"{greeting}, {name}!")
    
greet("Alice", greeting="Hanji")