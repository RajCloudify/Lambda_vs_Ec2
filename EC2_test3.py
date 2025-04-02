import time
import json

def run_test():
    # Create dummy data
    data = {"users": [{"id": i, "name": f"User{i}"} for i in range(10000)]}

    start = time.time()
 
    # Simulate receiving JSON string
    json_string = json.dumps(data)
    parsed = json.loads(json_string)

    # Filter users with even IDs
    filtered = [user for user in parsed["users"] if user["id"] % 2 == 0]

    end = time.time()

    return {
        "filtered_count": len(filtered),
        "time_sec": round(end - start, 4)
    }

if __name__ == "__main__":
    result = run_test()
    print("Filtered Users:", result["filtered_count"])
    print("Execution Time (s):", result["time_sec"])
                                                                                                                                                                                                                                                                                     
