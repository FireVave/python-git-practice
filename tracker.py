import sqlite3


def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_expense(item, amount, category):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (item, amount, category) VALUES (?, ?, ?)",
        (item, amount, category),
    )
    conn.commit()
    conn.close()
    print(f"Added: {item} (€{amount:.2f}) [{category}]")


def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, item, amount, category FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses found.")
        return

    for row in rows:
        print(f"[{row[0]}] {row[1]} - €{row[2]:.2f} ({row[3]})")


if __name__ == "__main__":
    init_db()
    add_expense("Coffee", 3.50, "Food")
    view_expenses()
