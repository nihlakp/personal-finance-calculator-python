print("===== Personal Finance Calculator =====")

name = input("Enter your name: ")

income = float(input("Enter your monthly income: ₹"))
rent = float(input("Enter your rent expense: ₹"))
food = float(input("Enter your food expense: ₹"))
transport = float(input("Enter your transport expense: ₹"))
other = float(input("Enter your other expenses: ₹"))

total_expenses = rent + food + transport + other
savings = income - total_expenses
savings_percentage = (savings / income) * 100

print("\n===== Financial Report =====")
print("Name:", name)
print("Monthly Income: ₹", income)
print("Total Expenses: ₹", total_expenses)
print("Savings: ₹", savings)
print("Savings Percentage:", round(savings_percentage, 2), "%")
