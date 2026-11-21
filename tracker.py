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


def add_expenses(item, amount, category):
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


def delete_expenses(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM expenses where ID = ?", (expense_id,)
    )  # cursor execute strictly requires a touble or list as its second arguement (5,) is what tells pyhton that "this is a 1-item tuple"
    conn.commit()
    change_checker = cursor.rowcount
    conn.close()

    if change_checker == 0:
        print(f"NO expence found with ID {expense_id}")

    else:
        print(f"Deleted expence [ {expense_id}. ]")


def main():
    init_db()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            item = input("Item name: ").strip()
            try:
                amount = float(input("Amount (€): "))
            except ValueError:
                print("Invalid amount. Please enter a number (e.g., 4.50).")
                continue
            category = input("Category (e.g., Food, Transport): ").strip()
            add_expenses(item, amount, category)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_expenses()
            try:
                expense_id = int(input("Enter the ID to delete: "))
            except ValueError:
                print("Invalid ID. Please enter a whole number.")
                continue
            delete_expenses(expense_id)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please type 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
