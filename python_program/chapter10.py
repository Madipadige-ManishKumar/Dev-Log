# # Object Oriented Programming In Python
# #creating a Class
# class Class1:
#     def sum(self):
#         return self.a+self.b

# n1=Class1()  # creating the instance 
# n1.a=923
# n1.b=2039
# s=n1.sum()
# print(s)
class Railway:
    formtype="Railway"
    def __init__(self):  # it is constructor 
        print("It Is Constructor")
    def printData(self): # instance method 
        print(f"The Name is {self.name}")
        print(f"The train is {self.train}")
    def greet():  # static method
        print("Good Morning have a Good Day ")
obj1=Railway()
obj1.name="Manish"
obj1.train="Rajadhani"
obj1.printData()
Railway.greet() # call to static method by className
print(22//5)