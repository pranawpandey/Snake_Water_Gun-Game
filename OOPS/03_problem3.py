''' 3. Create a class with a class attribute a; create an object from it and set ‘a’
 directly using ‘object.a = 0’. Does this change the class attribute'''

class demo:
    a=4
o=demo()
print(o.a)      #prints the class attribute because the instance object is  not created.
 
o.a=0  # instance object is set and instance object is preffered over class attribute.

print(o.a)

print(demo.a)  #prints the class attribute

print("NO it will not change the class attribte")