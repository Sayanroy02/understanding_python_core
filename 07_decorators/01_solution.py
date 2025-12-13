import time

def timer(func):  # Decorator to measure the execution time of a function
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        total_time = end_time - start_time
        # time_value = round(total_time, 2)
        print(f"{func.__name__} ran in {total_time} time")  #func.__name__ gives the name of the function being decorated
        return result
    return wrapper


@timer
def function1(n):
    time.sleep(n)


function1(2)
