# List 

# list are same as array and you have to give the values in array 
a=[1,2,3,4,56,78]
# printing the list using the print 
print(a)
# accessing the elements by index 
print(a[1])
# changing the value using the  index 
print(a[0])
print("The Slicing 2 ",a[0:5:2])
a[0]=90
print(a[0])
# list slicing
print("The Slicing 1",a[1:3])

# a list can have different type of data 
b=[1,3.14,"Manish",True]
print(b)
# methods in list
print (a)
a.sort() #sort the list
print("Sorted List  ",a)
a.reverse()  # reverse the list 
print("revered List ",a)
a.append(7)  # adds the given  element the last or last 
print(a)
a.insert(3,51)  # a.insert(index ,element value ) 
print(a)
a.pop(4)# pop the element from given value in list 
print(a)

# Tuples 
# tuple is immutbale 
t=(1,2,3,4,5)
# the access the values in tuple 
print(t[0])
# we can't change the value in a tuple
# t[0]=7
# print(t)

# t1=()# tuple with no element 
# # t2=(1)# wrong way to declare the Tuple with single element 
# t1(1,)# correct way to declare the tuple with single element 
# print(t3)

print(t.count(5))
print(t.index(5))