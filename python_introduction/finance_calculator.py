'''This script will calculate the user’s monthly savings 
based on inputted monthly income and expenses. 
It will then project these savings over a year,
assuming a fixed interest rate,
to demonstrate compound interest’s effect on savings.'''

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income- monthly_expenses

# Calculate the projected savings after one year.
# incorporating the interest, Assume a simple annual interest rate of 5%.
projected_savings = monthly_savings * 12 * 1.05

print("Your monthly savings are","$"+str(int(monthly_savings))+".")
print("Projected savings after one year, with interest, is:","$"+str(int(projected_savings))+".")