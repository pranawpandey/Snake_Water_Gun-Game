a= int (input ("enter a num "))
fact = 1
if a < 0:
    print("factorial does not exist")
elif a==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact= fact*i
        print(fact)
        
