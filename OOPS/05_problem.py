# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

import random
class Train:
    def __init__(self,train_no):
        self.train_no=train_no
        
    def book(self,train_no,fro,to):
        print(f"The Ticket is booked in {self.train_no}, from {fro} to {to}")
    def getstatus(self,train_no):
        print(f"Train_num {self.train_no} is running on time")
    def getfare(self,train_no,fro,to):
        print(f"The Ticket fare booked in {self.train_no}, from {fro} to {to} is {random.randint (220,600)} ")
    

T= Train(15159)
T.book(15159,"Reoti","Delhi")
T.getstatus(15159)
T.getfare(15159,"Reoti","Delhi")
