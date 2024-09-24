# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):
    for i in range(n+1):
        print("*" *(n-i +1))
n= int(input("enter the value of n: "))
print(pattern(n))



