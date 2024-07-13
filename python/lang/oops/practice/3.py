# does the class attribute value change
class demo:
    a=4

obj=demo()

# using object =4
print(obj.a)

obj.a=0

# using obj instance =4
print(obj.a) #instance attribute is set as another refference on the place of class atrribute as their refference is different so its just another version for obj instance

# using class name =4 
print(demo.a)