import sqlite3

def filter_groups_with_having():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #1
    query = "SELECT category, COUNT(*) AS total_products FROM products GROUP BY category HAVING COUNT(*) >= 2"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    filter_groups_with_having()