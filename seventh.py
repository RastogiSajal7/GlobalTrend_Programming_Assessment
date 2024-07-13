import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper
@measure_execution_time
def calculate_square(num):
    time.sleep(1)
    return num ** 2
result = calculate_square(5)
print(f"The square is: {result}")
