import requests
import sqlite3
import time
from datetime import datetime, timedelta


def sleep():
    now = datetime.now()
    # Floor to the current 10-minute mark
    floored = now.replace(minute=(now.minute // 10) * 10, second=0, microsecond=0)
    # Add 10 minutes to get the *next* 10-minute mark
    next_mark = floored + timedelta(minutes=10)
    # Compute how many seconds to sleep
    sleep_seconds = (next_mark - now).total_seconds()
    print(f"Sleeping for {sleep_seconds:.2f} seconds until {next_mark}")
    time.sleep(sleep_seconds)
    


API_URL = "https://api.hypixel.net/v2/skyblock/bazaar"  #
DATABASE_NAME = "bazaar_history.db"
TABLE_NAME = "quick_status"
REQUEST_INTERVAL = 600  # Interval between API requests in seconds

# Create database
conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        productId TEXT,
        sellPrice REAL,
        sellVolume INTEGER,
        sellMovingWeek INTEGER,
        sellOrders INTEGER,
        buyPrice REAL,
        buyVolume INTEGER,
        buyMovingWeek INTEGER,
        buyOrders INTEGER,
        timestamp TEXT
    )
''')

cursor.execute(f'''
    CREATE INDEX IF NOT EXISTS idx_product_time ON {TABLE_NAME}(productId, timestamp);
''')

conn.commit()
conn.close()


while True:
    sleep()
    try:
        print("Requesting data from Bazaar")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        products = data.get("products", {})
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M")

        print("Connecting to database")
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        print("Saving data")
        for product in products.values():
            qs = product.get("quick_status")
            if not qs:
                continue

            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} (
                    productId, sellPrice, sellVolume, sellMovingWeek,
                    sellOrders, buyPrice, buyVolume, buyMovingWeek,
                    buyOrders, timestamp
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                qs["productId"],
                qs["sellPrice"],
                qs["sellVolume"],
                qs["sellMovingWeek"],
                qs["sellOrders"],
                qs["buyPrice"],
                qs["buyVolume"],
                qs["buyMovingWeek"],
                qs["buyOrders"],
                timestamp
            ))

        # Delete data older than 7 days
        cursor.execute(f'''
            DELETE FROM {TABLE_NAME}
            WHERE timestamp < datetime('now', '-7 days')
        ''')

        conn.commit()
        conn.close()
        print(f"[{timestamp}] Stored {len(products)} entries. Old records cleaned.")

    except Exception as e:
        print("Error while getting data:", e)

    time.sleep(10)
      
