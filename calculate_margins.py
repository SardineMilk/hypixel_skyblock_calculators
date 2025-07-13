import sqlite3


DATABASE_NAME = "bazaar_history.db"
TABLE_NAME = "quick_status"

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

try:
    cursor.execute(f"ALTER TABLE {TABLE_NAME} ADD COLUMN maxProfit REAL")
    print("maxProfit column created")
except sqlite3.OperationalError as e:
    pass

cursor.execute(f"""
    UPDATE {TABLE_NAME}
    SET maxProfit = 
        (buyPrice - sellPrice) *
        (
            CASE 
                WHEN buyMovingWeek < sellMovingWeek THEN buyMovingWeek
                ELSE sellMovingWeek
            END
            / (24.0 * 7)
        )
""")

print("maxProfit column populated successfully.")


"""

"""


cursor.execute(f"""
    SELECT 
        productId,
        sellPrice,
        (sellMovingWeek/ (7*24)) AS sellVolume,
        buyPrice,
        (buyMovingWeek/ (7*24)) AS buyVolume,
        maxProfit
               
    FROM {TABLE_NAME}

    WHERE timestamp = (
        SELECT MAX(timestamp)
        FROM {TABLE_NAME}
    )

    ORDER BY maxProfit DESC;
""")
items = cursor.fetchall()

print("productId, sellPrice, sellVolume, buyPrice, buyVolume, maxProfit")
for item in items[0:50]:
    print(item)


# Commit and close
conn.commit()
conn.close()
