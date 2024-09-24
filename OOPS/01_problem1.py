# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft

class employee():
    company="Microsoft"
    def __init__(self, name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode
p=employee("pranaw",120000,277209)
print(p.name,p.salary,p.pincode,p.company)