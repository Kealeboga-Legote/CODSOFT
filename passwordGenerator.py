import random
import string

def validPassword(string):
    if string and string[0].isalpha(): #isalpha() - used to check whether all the characters in a given string are alphabetic characters (letters) or not
        return True
    else:
        return False

print("Welcome to the PASSWORD GENERATOR")
passwordLength = int(input("Specify the desired length of the password: "))

randomSpecial = ""
specials ="!@#$%&*_.><~"
for k in range(passwordLength):
    randomSpecial = randomSpecial + random.choice(string.ascii_letters + specials + string.digits)

while validPassword(randomSpecial) == False and randomSpecial.find(specials) == -1 :
    randomSpecial=""
    for v in range(passwordLength):
        randomSpecial = randomSpecial + random.choice(string.ascii_letters + specials + string.digits)
else :
    print("Your new password is:", "'" +randomSpecial+ "'")

