def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


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

def view_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Expenses ---")
            for line in file:
                item, amount = line.strip().split(",")
                print(item, ":", amount)
                total += int(amount)

        print("Total Spent:", total)
    except:
        print("No expenses found!")

