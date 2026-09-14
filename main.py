print("====== EXPENSE TRACKER ======")
print("1. Add Expense")
print("2. View Expense")
print("3. Total Expense")
print("4. Exit")

x = input("Enter your choice: ")
print(x)

expenses =[]

if x == "1":
    print("Add expense selected!")
    expense_name = input("Enter Expense Name: ")
    amount= float(input("Enter Amount:"))
    category = input("Enter Category:")
    expenses.append([expense_name,amount,category])
    print("Expense added succesfully!")
    
elif x == "2":
    for expense in expenses:
        print(expense)
    print("View expense selected!")
elif x == "3":
    print("Total expenses")
elif x == "4":
    print("Exit")
else:
    print("Invalid choice")