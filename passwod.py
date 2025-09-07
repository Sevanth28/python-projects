import random
import string
print("Welcome to password genarator !")
print("There are three levels \n Select 1 for easy \n Select 2 for medium \n Select 3 for hard")
choice=int(input("Enter your choice :"))
if choice==1:
  character=string.digits
elif choice==2:
  character =string.digits+string.ascii_letters
elif choice==3:
  character=string.ascii_letters+string.digits+string.punctuation
else:
  print("Invalid entry hence redirecting to strong password")
  character=string.ascii_letters+string.digits+string.punctuation
len=int(input('Enter the password length:'))
password=''.join(random.choice(character)  for _ in range (len))
print("Your password is :",password)
save=input("do you want to save this password file ?(y/n):")
if save.lower()=="y":
  with open("pass.txt","a") as file:
    file.write(password +"\n")
    print("Password saved to passswords.txt")