import time
import requests

def run_test():
    start = time.time()
    urls = ["https://httpbin.org/get"] * 10  # 10 simple GETs
    for url in urls:
        _ = requests.get(url)
    end = time.time()
    return {
        "requests": len(urls),
        "time_sec": round(end - start, 4)
    }

if __name__ == "__main__":
    result = run_test()
    print("Total Requests:", result["requests"])
    print("Total Time (s):", result["time_sec"])
~                                                    
