arr=[]
while True:
    print("Welcome to do-list !")
    print("1 - To add tasks")
    print("2 - To remove tasks")
    print("3 - To view tasks")
    print("4 - Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        task=input("Enter the task")
        arr.append(task)
    elif choice==3:
        for i in arr:
            print(i)   
    elif choice==2:
        reo=input("Enter the task to remove:")
        for i in arr:
            if reo==i:
               arr.remove(i)
            else:
                print("Task not found")
    else:
        print("Thank you !!!")
        break                   

    
        
