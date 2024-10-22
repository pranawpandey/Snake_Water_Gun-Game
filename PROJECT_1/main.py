import random

'''
1 for snake
-1 for water
0 for gun
'''

computer=random.choice([1,-1,0])  # computer will choose random numbers between the three numbers
youstr=input("enter your choice: ")
youdict={"s":1 , "w":-1 , "g":0}
reverseddict={1:"Snake" , -1:"Water" , 0:"Gun"}

you=youdict[youstr]
 
 # by now we have two numbers(variables) that is you and computer

print(f"You chose {reverseddict[you]}\nComputer chose {reverseddict[computer]}")

if(computer==you):
    print("Its a Draw! ")
else:
    if(computer==-1 and you==1):
        print("you win!") #
    if(computer==0 and you==-1):
        print("you win!") #
    if(computer==1 and you==-1):
        print("you loose!")
    if(computer==-1 and you==0):
        print("you loose!")
    if(computer==0 and you==1):
        print("you loose!")
    if(computer==1 and you==0):
        print("you win!") #
