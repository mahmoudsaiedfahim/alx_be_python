'''This calculator will prompt the user to enter 
two numbers and select an operation 
(addition, subtraction, multiplication, or division). 
The script will then perform the selected operation 
using a Match Case statement and display the result.'''
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = first_number+second_number
        print(result)
    case "-":
        result = first_number-second_number
        print(result)
    case "*":
        result = first_number*second_number
        print(result)
    case "/":
        if second_number !=0:
            result = first_number/second_number
            print(result)
        else:
            print("Cannot divide by zero.")
