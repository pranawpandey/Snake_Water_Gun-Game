# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class calculator():
    def __init__(self,number):
        self.number=number
        
    def square(self):
        print(f"the square is: {self.number*self.number}")
    def cube(self):
        print(f"the cube is: {self.number*self.number*self.number}")
    def sqrt(self):
        print(f"the sqrt is: {self.number**1/2}")
num=calculator(4)
num.square()
num.cube()
num.sqrt()