print("====== EXPENSE TRACKER ======")
print("1. Add Expense")
print("2. View Expense")
print("3. Total Expense")
print("4. Exit")

x = input("Enter your choice: ")
print(x)

if x == "1":
    print("Add expense selected!")
elif x == "2":
    print("View expense selected!")
elif x == "3":
    print("Total expenses")
elif x == "4":
    print("Exit")
else:
    print("Invalid choice")