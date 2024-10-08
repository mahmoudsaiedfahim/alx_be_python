'''This script will demonstrate your ability to 
use the datetime module for handling dates and times 
in Python.'''
from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    return datetime.now()

def calculate_future_date(number_of_days):
    return datetime.now()+timedelta(days=number_of_days)

current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
number_of_days=int(input("Enter the number of days to add to the current date: "))
future_date=calculate_future_date(number_of_days)
print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
