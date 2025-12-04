import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        total_time = end_time - start_time
        # time_value = round(total_time, 2)
        print(f"{func.__name__} ran in {total_time} time")
        return result
    return wrapper


@timer
def function1(n):
    time.sleep(n)


function1(2)
