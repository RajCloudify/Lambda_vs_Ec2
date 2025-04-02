import time, os, psutil

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

start = time.time()
result = fib(30)
end = time.time()

process = psutil.Process(os.getpid())
mem = process.memory_info().rss / (1024 * 1024)  # in MB

print("Result:", result)
print("Time (s):", end - start)
print("Memory (MB):", mem)
