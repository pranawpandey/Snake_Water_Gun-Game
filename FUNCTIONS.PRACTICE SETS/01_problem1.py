# . Write a program using functions to find greatest of three number

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a=int(input("enter the number: " ))
b=int(input("enter the number: " ))
c=int(input("enter the number: " ))
print(f"The greatest number among the three is: {greatest(a,b,c)}")
