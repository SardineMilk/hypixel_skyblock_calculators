import requests
import json
import datetime
import time

print("Running")

REQUEST_INTERVAL = 10

requested = []
while True:
    request_timestamp = datetime.datetime.now()
    file_name = "raw_bazaar_data/"
    file_name += str(request_timestamp.year)
    file_name += "_" + str(request_timestamp.month)
    file_name += "_" + str(request_timestamp.day)
    file_name += "_" + str(request_timestamp.hour)
    file_name += "_" + str(request_timestamp.minute)
    file_name += ".json"

    if (file_name not in requested) and ((request_timestamp.minute % REQUEST_INTERVAL) == 0):
        print("Querying Hypixel API...")
        print(f"Timestamp: {request_timestamp}")
        response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
        response.raise_for_status()
        print("Query Complete")

        print("Saving Query Data...")
        data = response.json()

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print("Query Data Saved")

        requested.append(file_name)

    time.sleep(10)

