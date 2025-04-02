import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def lambda_handler(event, context):
    start = time.time()
    result = fib(30)
    end = time.time()

    return {
        'result': result,
        'time_sec': end - start
    }
 
