'''In this script, define a function that performs 
basic arithmetic operations. 
This function, perform_operation, 
will be imported and used in a separate main.py'''

def perform_operation (num1: float, num2: float, operation: str):
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        case _ :
            result = "Error: Invalid Operation"
    return result