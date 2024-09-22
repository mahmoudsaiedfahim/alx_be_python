'''This script will ask the user to enter a number, 
then use a for loop to print the multiplication table 
for that number from 1 to 10.'''

number = int(input("Enter a number to see its multiplication table: "))
for iter in range(1,11):
    product = number * iter
    print(f"{number} * {iter} = {product}")