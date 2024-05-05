import math
import sys

def subtraction (x,y):
    return x -y

def addition(x,y):
    return x + y

def division(x,y):
    if y == 0:
        return "Error! Cannot divide by 0"
    else:
        if x%y != 0:
            wholeNum = x//y
            rem = x%y
            floating = x/y
            return str(wholeNum) + " with a remainder of " + str(rem) + " OR " + str(floating) 
        else:
            return x//y      

def multiplication(x,y):
    return x*y

print("Welcome to THE BASIC CALCULATOR!")
print("This calculator can perform 4 basic operations." + "\n"  )
 

def options():
      
      print("(1) Addition (+)" + "\n" +
      "(2) Subtraction (-)" + "\n" +
      "(3) Multiplication (x)" + "\n" +
      "(4) Division (÷)" + "\n" +
      "(5) Exit" + "\n")
      operation = int(input("Select the number of the operation you wish to perfom:"))
      validOptions = [1,2,3,4,5]
      if operation in validOptions:
        return operation
      else:
          return None
      


def selectionSwitchCase(option):
    first_int = int(input("Enter first number:"))
    second_int = int(input("Enter second number:"))
    if option == 1:
        return str(addition(first_int, second_int))
    elif option == 2:
        return str(subtraction(first_int, second_int))
    elif option == 3:
        return str(multiplication(first_int, second_int))
    elif option == 4:
        return str(division(first_int, second_int))
    

    
    
selection = options() 
isExit= False
while isExit==False:
    if selection == 5:
        print("You have choosen to exit." + "\n" +
            "Bye!")
        isExit=True
        exit()  

    elif selection == None:
        print("\n" + "You have made an invalid selection. Please try again" + "\n" )   
        selection = options()  
    else:
        ans = selectionSwitchCase(selection)
        print("The answer is:",ans)
        reCalc = int(input("Would you like to perform another calculation?" + "\n" +  "yes - (1) OR no - (0): "))
        if reCalc == 1:
            selection = options()
        elif reCalc == 0:
            print("You have choosen to exit." + "\n" +
            "Bye!")
            isExit=True
            exit()
        else:
            print("\n" + "You have made an invalid selection. Please try again" + "\n" )
    

  



        







