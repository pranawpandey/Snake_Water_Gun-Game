#Write a recursive function to calculate the sum of first n natural numbers
 
def sum(n):
    if(n==1):  #base case
     return 1
    return sum(n-1)+n
n= int(input("enter the number: "))
print(f" The sum is: {sum(n)}")