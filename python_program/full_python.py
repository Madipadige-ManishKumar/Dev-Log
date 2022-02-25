'''
This is python multi line  comment 
'''

def printh(v):
    print(f"\033[1m\033[34m{v}\033[0m")

# The is A comment in   the python code  single line comment


# in python code  we don't have any kind of declaration of a variable
# we only have the assigning of the variable

x=7
y='7'
if(x==y):
    print("true ")
apple=banana="furit"
print(apple)
print(banana)

# unpacking in Python code
printh("Unpacking")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)  # we can also use the + operator but the result will be  concatenated

printh("Global variables")

x = 10  # This is a global variable
def func1():
    x=20
    print(f"This is a local variable {x}")
def func():
    # print(x)
    global x
    x=20  # changing the value of this global variable
    print(x)
func()
print(x)
func1()

printh("Data types in python")
class My_dataTypes():

    bool_data_type=True

    my_dict={
        'Key': 'value',
        'name': 'Madipadige Manish kumar',
        'pin':'21001-CS-007',
        'rank':'1'
    }
    def My_str(self):
        print("This is  a string variable")
    def My_numeric_data_type(self):
        x=7
        y=7.0
        z=complex(0,7)
        print(x,y,z)    
    def Sequence_data_type(self):
        my_list=[]  # empty list
        my_list=[1,2,3]
        print(my_list)
        my_tuple=tuple() # empty tuple
        my_tuple=(1,2,3)
        print(my_tuple)
        my_range=list(range(6))  # range data type
        print(my_range)
    
my_data_type = My_dataTypes()  # object creation  in python 
my_data_type.My_str()
my_data_type.My_numeric_data_type()
print(my_data_type.bool_data_type)
my_data_type.Sequence_data_type()
# accessing the dictionary from the class

print(my_data_type.my_dict['name'])
print(my_data_type.my_dict['rank'])
print(my_data_type.my_dict['pin'])

printh("Negative value in python")
z=-346752
print(z)
if (7):  # python 8ilo etla itha dhi 
    print("True")

def special_operator():
    x=1/2 # float  type 
    y=1//2  # int  type 
    print(x,y)
    x=1*2  # multiplication 
    print(x)
    y=1**2  # 1 power of 2 
special_operator()


print("Classes and Objects ")
printh("Inheritence in python ")
class parent_class():
    def __init__(self):
        print("This is the parent class")
class child_class(parent_class):
    def __init__(self):
        super().__init__() # super function 
        print("This is the child class")
child_class1=child_class()  # creation of object 

print("This is iterators")
mylist=[1,2,3]
myl=iter(mylist)

print(next(myl))
print(next(myl))


printh("Module in python ")
import rough as r
print(r.x)  # using the function of that module 

printh("datetime module ")
from datetime import *
def date_module():
    dt=datetime.now() # current date and time 
    print(dt)
    dt=datetime(2024,2,13,12,14,56)
    print(dt)
    
date_module()

printh("Math  Module ")
def math_module():
    import math
    print(math.pi)
    print(math.e)
    print(math.sin(math.pi/2))
    print(math.cos(math.pi/2))
    print(math.tan(math.pi/2))
    print(math.asin(1))
    print(math.acos(1))
    print(math.atan(1))
    print(math.ceil(3.1))
    print(math.floor(3.1))
    print(math.sqrt(9))
    print(math.log(9))
    print(math.log10(9))
    print(math.log2(9))
    # print(math.abs(-7))
math_module()

printh("Exception handling  in python ")
def Exception_handling():
    # in this we have Try,except ,else,finally
    try:
        a=10
        b=0
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both numbers must be numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(result)
    finally:
        print("This code block has finished executing.")

# Test the function with valid inputs
Exception_handling()




printh("Explict Exception Calling ")
def explict_calling_of_exception():
    try:
        c=7/0
        raise ZeroDivisionError("There is Zero division error")
    except Exception as e:
        print(f"An exception occurred: {e}")
    else:
        print(c)
    finally:
        print("compeleted")
explict_calling_of_exception()


printh("User defined exception")
class my_expect(Exception):
    pass
def user_defined_expect():
    try:
        c=7/0
        raise my_expect("There is Zero division error")
    except Exception as e:
        print(f"An exception occurred: {e}")
    else:
        print(c)
    finally:
        print("compeleted")
user_defined_expect()


printh("Threads in Python ")
from threading import *   # we use threading module to use the thread 
from time import *
'''  
Thread
def : in python  thread is a spefic part of  the  code which can exeute independently from  other code sinnept 
theroy{
In python thread is executed bhy the threading module 
}
to create a thread use the Thread Constructor function 

in threads we have the multiple methods like start,join,isAlive,getName,setName,activeCount and currentThread ant e.t.c

In Thread Syncronization we have to First create a lock  by that we have to  make  the synchronization


basically the threads have issues like race condition and deadlock
to avoid race   condition we use the concept called lock  which can  be implemented using the lock class 
lock class have the methods like acquire ,release
'''

def Thread_my_function_square(n):
    for i in range(n):
        print("The Current Thread is",Thread.name,"The i th value  the square of it is  ",(i*i))
        sleep(1)
def Thread_my_function_cube(n):
    for i in range(n):
        print("The Current Thread is",Thread.name,"The i th value  the Cube of it is  ",(i*i*i))
        sleep(1)


Thread1 = Thread(name="thread1",target=Thread_my_function_square,args=(5,))
print("The Name of Thread one is ",Thread1.name) # Accessing the Name 

Thread2 = Thread(name="Thread2",target=Thread_my_function_cube,args=(5,))
print("The Name of Second thread is ",Thread2.name)
print("The Thread1 is alive",Thread1.is_alive())
print("The Thread2 is alive",Thread2.is_alive())
Thread1.start()
print("The Thread1 is alive",Thread1.is_alive())
print("The Thread2 is alive",Thread2.is_alive())
Thread2.start()  # start 
Thread1.join()
Thread2.join()   # join
