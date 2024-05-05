import pickle

class ToDoList:

    def __init__(self):
        self.tasks = []

    def loadListFromFile(filePath):
        try:
            with open(filePath, 'rb') as listFile:
                return pickle.load(listFile)
        except FileNotFoundError:
            return []

    def addTask(self, item):
        self.tasks.append(item)
        print("Task added successfully")

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
                print("Your To-Do List is empty")

    def saveList(filePath, toDoList):
        with open(filePath, 'wb') as listFile:
            pickle.dump(toDoList, listFile)

def main():
    classConstructor = ToDoList()
    filePath = 'todoList.pkl'

    print("Welcome to your To-Do list")
    print("Here are your current tasks:")

    def userInput():
        print("(1) Add a Task" + "\n" +
                "(2) Remove a task" + "\n" +
                "(3) Show current tasks" + "\n" +
                "(4) Exit" + "\n" )
        operation = int(input("Select the number of the acion you choose to do:"))
        validOptions = [1,2,3,4]
        if operation in validOptions:
            return operation
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
    loaded = loadListFromFile(filePath)
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
            selectionSwitchCase(selection)
        
            reCalc = int(input("Would you like to Add, Remove or Show tasks?" + "\n" +  "yes - (1) OR no - (0): "))
            if reCalc == 1:
                selection = userInput()
            elif reCalc == 0:
                saveList(filePath)
                print("You have choosen to exit." + "\n" +
                "Bye!")
                isExit=True
                exit()
            else:
                print("\n" + "You have made an invalid selection. Please try again" + "\n" )