# 4. Add a static method in problem 2, to greet the user with hello.



class calculator():
    def __init__(self,number):
        self.number=number
        
    def square(self):
        print(f"the square is: {self.number*self.number}")
    def cube(self):
        print(f"the cube is: {self.number*self.number*self.number}")
    def sqrt(self):
        print(f"the sqrt is: {self.number**1/2}")
    @staticmethod
    def hello():
        print("Hello There!")
    
num=calculator(4)
num.hello()
num.square()
num.cube()
num.sqrt()
