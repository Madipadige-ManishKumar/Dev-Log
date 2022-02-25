'''
Types Of Function 
Built_in
user_defined 
'''

#functoin Defination

# # recursive Function
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1) 
    

def Percent(Marks):
    return (sum(Marks)/400*100)
def Add(num1,num2=0): # default Parameter Value 
    print(num1+num2)
Marks=[90,87,89,79]
p=Percent(Marks)# function call
Marks1=[90,87,89,79]
p1=Percent(Marks1)# function call
print(p,p1)
Add(1,2)
Add(2)

# Quick Quiz 
def Hello(name ):
    print("Good Day",name)
name=str(input("Enter Name "))
Hello(name)

n=int(input("Enter A Number"))
print(fact(n))

