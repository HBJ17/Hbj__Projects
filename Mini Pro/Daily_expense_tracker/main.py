def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Exit")

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        print("Add expense selected")
    elif choice == "2":
        print("Bye!")
        break
    else:
        print("Invalid choice")

def add_expense():
    item = input("Item name: ")
    amount = input("Amount: ")

    with open("expenses.txt", "a") as file:
        file.write(item + "," + amount + "\n")

    print("Expense saved!")

# connect to menu
if choice == "1":
    add_expense()
