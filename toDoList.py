myTasks= []

def addTask(item):
    myTasks.append(item)
    print("Task added successfully")

def removeTask(item):
    if item in myTasks:
        myTasks.remove(item)
        print("Task removed successfully")
    else:
        print("Task not found")

def showTasks():
    if myTasks:
        print("Your To-Do List:")
        for index, task in enumerate(myTasks, start=1):
            print(f"{index}. {task}")
    else:
            print("Your To-Do List is empty")

print("Welcome to your To-Do list")
print("Here are your current tasks:")

def userInput():
      print("(1) Add a Task" + "\n" +
            "(2) Remove a task" + "\n" +
            "(3) Show current tasks" + "\n" +
            "(4) Exit" + "\n" )
      operation = int(input("Select the number of the operation you wish to perfom:"))
      validOptions = [1,2,3,4]
      if operation in validOptions:
        return operation
      else:
          return None
      
def selectionSwitchCase(option):
    if option == 1:
        userTask = input("Enter new task:")
        addTask(userTask)
    elif option == 2:
        userTask = input("Enter task to remove:")
        removeTask(userTask)
    elif option == 3:
        showTasks()

selection = userInput() 
isExit= False
while isExit==False:
    if selection == 4:
        print("You have choosen to exit." + "\n" +
            "Bye!")
        isExit=True
        exit()
    elif selection == None:
        print("\n" + "You have made an invalid selection. Please try again" + "\n" )   
        selection = userInput()
    else:
        ans = selectionSwitchCase(selection)
        print("The answer is:",ans)
        reCalc = int(input("Would you like to perform another calculation?" + "\n" +  "yes - (1) OR no - (0): "))
        if reCalc == 1:
            selection = userInput()
        elif reCalc == 0:
            print("You have choosen to exit." + "\n" +
            "Bye!")
            isExit=True
            exit()
        else:
            print("\n" + "You have made an invalid selection. Please try again" + "\n" )