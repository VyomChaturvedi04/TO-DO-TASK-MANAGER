todo=[]

def add():
    taskname=input("\nENTER YOUR TASK : \n\n""")
    todo.append({"TASK":taskname,"STATUS":"PENDING"})
    print("\n<>-<> TASK ADDED! <>-<>\n")

def view():
    print("\nYOUR TO-DO LIST\n")
    if len(todo)==0:
        print("NO TASKS YET\n") 
    else:
        print("No. | Task Name | Status")
        print("----|-----------|--------")
        for index,taskname in enumerate(todo,1):
            print(f" {index:<2} | {taskname['TASK']:<9} | {taskname['STATUS']}")

def update():
    if len(todo) == 0:
        print("\nLIST IS EMPTY, NOTHING TO UPDATE!\n\n""")
        return    
    try:
        update_task_num=input("\nENTER TASK NUMBER FOR UPDATION : \n\n""")
        searchind = int(update_task_num)- 1
        if 0 <= searchind < len(todo):
            up = input("\nENTER NEW TASK DESCRIPTION : \n\n""")
            oldtask = todo[searchind]['TASK']
            todo[searchind]['TASK'] = up
            print(f"\nTASK [",{searchind + 1},"] UPDATED!\n\n""")
            print(f"Old Task: {oldtask}")
            print(f"Updated Task: {up}")
        else:
            print("\nINVALID TASK NUMBER!\n\n""")
            
    except ValueError:
        print("\nPLEASE ENTER A VALID NUMBER FOR THE TASK!\n\n""")
    except Exception as e:
        print(f"\nAN UNEXPECTED ERROR OCCURED: {e}\n\n""")           

def delete():
    if len(todo)==0:
        print("\nLIST IS EMPTY\n")
    else:
        try:
            searchind=int(input("\nENTER TASK NUMBER FOR DELETION : \n\n"""))-1  
            if 0<= searchind<len(todo):
                delete_task=todo.pop(searchind)
                print(f"\nTASK REMOVED : {delete_task['TASK']}\n\n""")
            else:
                print("\nINVALID TASK NUMBER!\n\n""")  
        except ValueError:         
            print("\nENTER VALID TASK NUMBER\n\n""") 

def done():
    if len(todo)==0:
        print("\nLIST IS EMPTY!\n\n""")
    else:
        try:
            searchind=int(input("\nENTER TASK NUMBER TO MARK COMPLETE  : \n\n"""))-1  
            if 0<= searchind<len(todo):
                todo[searchind]['STATUS']='DONE'
                print("\nTask {todo[searchind]['TASK']} HAS BEEN MARKED AS DONE\n\n""")     
            else:
                print("\nINVALID TASK NUMBER!\n\n""")  
        except ValueError:         
            print("\nENTER VALID TASK NUMBER\n\n""")

def menu():
    while(True):
        print("\n<>-<>-<> MENU <>-<>-<>\n")
        print("[1] ADD TASK")
        print("[2] VIEW TASKS")
        print("[3] UPDATE TASK")
        print("[4] DELETE TASK") 
        print("[5] MARK TASK COMPLETE")
        print("[6] EXIT\n")

        opr=input("ENTER OPERATION : \n""\n""")
        if opr=="1":
            add()
        elif opr=="2":
            view()    
        elif opr=="3":
            update()  
        elif opr=="4":
            delete()        
        elif opr=="5":
            done()
        elif opr=="6":
            print("<>-<>-<> EXITING PROGRAM <>-<>-<>")
            exit()
        else:
            print("\nOPERATION DOES NOT EXIST.\n")    

menu()