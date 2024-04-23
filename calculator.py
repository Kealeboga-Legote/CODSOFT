import math

def subtraction (x,y):
    return x -y

def addition(x,y):
    return x + y

def division(x,y):
    if y == 0:
        return "Error! Cannot divide by 0"
    else:
        return x/y

def multiplication(x,y):
    return x*y

print("Welcome to Kealeboga's Calculator!")
first_int = int(input("Enter first number:"))
second_int = int(input("Enter second number:"))

print("1. Addition (+)" + "\n" +
      "2. Subtraction (-)" + "\n" +
      "3. Multiplication (x)" + "\n" +
      "4. Division (÷)")
operation = input("Select the number of the operation you wish to perfom:").split()

if operation == 1:
    print("The answer is: ", addition(first_int, second_int))
elif operation == 2:
    print("The answer is: ", subtraction(first_int, second_int))
elif operation == 3:
    print("The answer is: ", multiplication(first_int,second_int))
else:
    print("The answer is: ", division(first_int, second_int))

