import sqlite3
import matplotlib.pyplot as plt
import datetime


DATABASE_NAME = "bazaar_history.db"
TABLE_NAME = "quick_status"

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

cursor.execute(f"SELECT DISTINCT productId FROM {TABLE_NAME}")
items = [row[0] for row in cursor.fetchall()]  # List of product names



for item in items:
    cursor.execute(f"""
        SELECT timestamp, buyPrice, sellPrice
        FROM {TABLE_NAME}
        WHERE productId = ?
        ORDER BY timestamp, maxProfit
    """, (item,))
    
    data = cursor.fetchall()
    
    if not data:
        continue  # skip if no data
    
    # Unpack into two lists: timestamps and prices
    timestamps, buy_prices, sell_prices = zip(*data)
    timestamps = [datetime.datetime.fromisoformat(ts) for ts in timestamps]  

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, buy_prices, label='Buy Price', marker='o', color='green')
    plt.plot(timestamps, sell_prices, label='Sell Price', marker='x', color='red')

    plt.title(f'Price Over Time for {item}')
    plt.xlabel('Time')
    plt.ylabel('Cost')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()



# Commit and close
conn.commit()
conn.close()
