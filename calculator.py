def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        print("Zero cannot used to divide!!")
while True:        
 print("Welcome to the calculator menu\n 1 to add\n 2 to substract\n 3 to muiltiply\n 4 to divide\n 5 to exit")
 choice=int(input("Enter your choice:"))
 if choice==5:
      print("Thank you for using the calculator")  
      break
 try:
  num1=float(input("Enter the first number:"))
  num2=float(input("Enter the second number:"))
 except ValueError:
  print("Invalid entry")
  continue
 if choice==1:
    print(add(num1,num2))
 if choice==2:
    print(sub(num1,num2))
 if choice==3:
    print(mul(num1,num2))
 if choice==4:
    print(div(num1,num2))       
     




