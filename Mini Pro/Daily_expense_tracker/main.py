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
