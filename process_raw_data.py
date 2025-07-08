import json
import csv
import os

raw_dir = "raw_bazaar_data"
processed_dir = "bazaar_data"

os.makedirs(processed_dir, exist_ok=True)

headers = ["productId","sellPrice","sellVolume","sellMovingWeek","sellOrders","buyPrice","buyVolume","buyMovingWeek","buyOrders"]

for file_name in os.listdir(raw_dir):
    raw_path = os.path.join(raw_dir, file_name)
    processed_file_name = file_name.replace('.json', '.csv')
    processed_path = os.path.join(processed_dir, processed_file_name)

    if  os.path.isfile(processed_path):
        print(f"Skipped {processed_file_name}")
        continue

    # Get the raw bazaar data
    with open(raw_path, 'r') as file:
        data = json.load(file)

    # Get the quick_status values for each item
    processed_data = []
    for id, item in data.get('products', {}).items():
        quick_status = item.get('quick_status', {})
        processed_data.append(list(quick_status.values()))

    # Sort alphabetically by item name
    processed_data.sort(key=lambda x: x[0])

    # Write quick_status of each item to csv file
    with open(processed_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(processed_data)

    print(f"Processed: {file_name} -> {processed_file_name}")
