#this program is a personal finance calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculate how much user saves in a month, by formula:
monthly_savings = monthly_income - monthly_expenses

#project annual savings assuming interest rate of 5%
#projected savings = monthly savings * 12 + (monthly savings * 12 * 0.05)
annual_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12) 

print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",annual_savings)
