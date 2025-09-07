import random
num=random.randint(1,10)
sur=int(input("Enter your guess :"))
att=1
while(num!=sur):
 print("Try again!!!")
 sur=int(input("Enter your guess :"))
 att=att+1
 num=random.randint(1,10)
print("You guessed it right on the ",att," attempt")