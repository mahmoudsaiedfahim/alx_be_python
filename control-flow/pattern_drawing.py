'''This script will prompt the user to enter 
a positive integer, then use nested loops to print 
a square pattern of that size made of asterisks (*).'''

length = int(input("Enter the size of the pattern: "))
row = 0
while row < length:
    for width in range (length):
        print("*",end="")
    print()
    row +=1