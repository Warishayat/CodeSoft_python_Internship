#PROJECT 2: Where i will make TO-DO-LIST APP
#CodeSoft_internship


todoList=[]                                         # initialized empty list
print("************Welcome to To-Do-List App******************")
def add_task(todoList):                                     #ADD TASK

    task=input("Enter the task you want to add: ")
    setter=task.lower()
    todoList.append(setter)
    print("Task Sucessfully added--->Updated To-Do-list is:",todoList)

def delete_task():                              #DELETE TASK
        try:                                    #error handle
            name=input("Enter the name of task that you want to delet:")
            getter=name.lower()       
            if name in todoList:
                todoList.remove(getter)
                print("Successfuly deleted!--> Updated to-do-list is:",todoList)
            else:
                print("Sorry !!! This is not avialable in list.")
        except ValueError:
            print("You make valueError here.")
            
            
def Showtask(todoList):                             #show list of total task
    print("****Your To-Do-List is****")
    for key,value in enumerate(todoList,start=1):
        print(f"{key}====>{value}")
    if todoList==0:
            print("Your list is empty")
#main

while True:
        try:
            choice=int(input("""
        Press 1 to add task.
        press 2 to delet task.
        press 3 to show all task.
        press 4 to shutdown the app.
        \n"""))
            if choice==1:
                add_task(todoList)
            elif choice==2:
                delete_task()
            elif choice==3:
                Showtask(todoList)
            elif choice==4:                         #discontinue program/leave
                try:
                    makechoice=input("Do you really want to close list (type y for brake else anykey for continue:)")
                    if makechoice.lower()=='y':
                        print("you sucesfully leave the app")
                        break
                    else:
                        pass        
                except ValueError:
                    print("You make some valueError.")
            else:
                print("You enter some invalid character:")
                continue
            
        except ValueError:
            print("You make some valueError:")
            continue