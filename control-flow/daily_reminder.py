'''This script will ask the user for a single task, 
its priority level, and if it is time-sensitive. 
The program will then provide a customized reminder 
for that task, demonstrating control flow and loops 
without relying on data structures to store 
multiple tasks.'''

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    
# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    reminder += ". Consider completing it when you have free time."
    print(f"Note: {reminder}")
