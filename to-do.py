
try:
    with open("task.txt", "r") as file:
        arr=[line.strip() for line in file.readlines()]
except FileNotFoundError:
    arr=[]

while True:
    print("1.To add task\n 2.To delete task\n 3.To view the task\n 4.To exit")
    cho=int(input("Enter your choice :"))
    if(cho ==1):
        t=input("Enter the task:")
        arr.append(t)
    elif(cho ==2):
        t=input("Enter the task to delete :")
        for t in arr:
            arr.remove(t)
    elif(cho==3):
        print("The tasks are :")
        for i,val in enumerate(arr,1):
            print(f"{i}.{val}")
    else:
        print("Thank you !")
        with open("text.txt","w") as file:
            for task in arr:
                file.write(task+"\n")
        print("The file saved successfully ")
        break
