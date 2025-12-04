import time


def cache(func):
    cache_value = {} # Dictionary to store cached results
    print(cache_value) # Initially empty
    def wrapper(*args):
        if args in cache_value: # Check if result is already cached
            return cache_value[args] # Return cached result
        result = func(*args)
        cache_value[args] = result # Cache the new result
        return result
    return wrapper



@cache
def add_function(a,b):
    time.sleep(5)
    return a+b

print(add_function(2,3))
print(add_function(2,3))
print(add_function(5,7))