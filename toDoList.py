import pickle

class ToDoList:

    def __init__(self):
        self.tasks = []

    

    def addTask(self, item):
        self.tasks.append(item)
        print("Task added successfully")
    
    def checkIntInput(self, input):
        try:
            intValue = int(input)
            return intValue
        except ValueError:
            return "Error: Please enter a valid number input"

    def removeTask(self, item):
        if item in self.tasks:
            self.tasks.remove(item)
            print("Task removed successfully")
        else:
            print("Task not found")

    def showTasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
                print("\n" + "Your To-Do List is empty" + "\n")

    

def main():

    classConstructor = ToDoList()
   
    print("Welcome to your To-Do list")
    print("Here are your current tasks:")
    classConstructor.showTasks()
    
    def userInput():
        print("(1) Add a Task" + "\n" +
                "(2) Remove a task" + "\n" +
                "(3) Show current tasks" + "\n" +
                "(4) Exit" + "\n" )
        operation = input("Select the number of the acion you choose to do:")
        validOptions = [1,2,3,4]
        result = classConstructor.checkIntInput(operation)
        if result in validOptions:
            return result
        else:
            return None
        
    def selectionSwitchCase(option):
        if option == 1:
            userTask = input("Enter new task:")
            classConstructor.addTask(userTask)
        elif option == 2:
            userTask = input("Enter task to remove:")
            classConstructor.removeTask(userTask)
        elif option == 3:
            classConstructor.showTasks()

    selection = userInput() 
   
    isExit= False
    while isExit==False:
        if selection == 4:
            print("You have choosen to exit." + "\n" +
                "Bye!")
            isExit=True
            exit()
        elif selection == None:
            print("\n" + "You have made an invalid selection. Please choose again" + "\n" )   
            selection = userInput()
        else:
            selectionSwitchCase(selection)
        
            reCalc = int(input("\n" + "Would you like to Add, Remove or Show tasks?" + "\n" +  "yes - (1) OR no - (0): "))
            if reCalc == 1:
                selection = userInput()
            elif reCalc == 0:
                
                print("You have choosen to exit." + "\n" +
                "Bye!")
                isExit=True
                exit()
            else:
                print("\n" + "You have made an invalid selection. Please try again" + "\n" )

if __name__ == "__main__":
    main()