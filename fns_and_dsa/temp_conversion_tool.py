'''This script will define functions to convert 
temperatures between Celsius and Fahrenheit, 
demonstrating the use of global variables to 
store conversion factors that are accessible 
within functions.'''

global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius*CELSIUS_TO_FAHRENHEIT_FACTOR+32
    

temperature=float(input("Enter the temperature to convert: "))
while type(temperature) is not float:
    temperature=float(input("Invalid temperature. Please enter a numeric value."))

unit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
while unit not in ["F","C"]:
    unit=input("Invalid temperature. Please enter a numeric value.")
if unit == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif unit == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")