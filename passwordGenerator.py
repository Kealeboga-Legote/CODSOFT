import random
import string

def validPassword(string):
    if string and string[0].isalpha(): #isalpha() - used to check whether all the characters in a given string are alphabetic characters (letters) or not
        return True
    else:
        return False
    
def checkIntInput(input):
        try:
            intValue = int(input)
            return intValue
        except ValueError:
            return -1


def passwordGen(passLength):
    
    randomSpecial = ""
    specials ="!@#$%&*_.><~"
    for k in range(passLength):
        randomSpecial = randomSpecial + random.choice(string.ascii_letters + specials + string.digits)

    while validPassword(randomSpecial) == False and randomSpecial.find(specials) == -1 :
        randomSpecial=""
        for v in range(passLength):
            randomSpecial = randomSpecial + random.choice(string.ascii_letters + specials + string.digits)
    else :
        output ="Your new password is:" + "'" +randomSpecial+ "'"
        return output


print("Welcome to the PASSWORD GENERATOR" + "\n")

def display():
    passwordLength = input("Specify the desired length of the password: ")
    result = checkIntInput(passwordLength)
    if result == -1 :
        print("Invalid entry. Please enter a numeric value.")
    else:
        ans = passwordGen(result)
        print(ans)

display()
isExit= False
while isExit==False:
        reCalc = input("\n" + "Would you like to generate another password?" + "\n" +  "yes - (1) OR no - (0): ")
        intRecalc = checkIntInput(reCalc)
        if intRecalc == 1:
            display()
        elif intRecalc == 0:
            print("You have choosen to exit." + "\n" +
            "Bye!")
            isExit=True
            exit()
        else:
            print("\n" + "You have made an invalid selection. Please enter either (1) OR (0)" + "\n" )

