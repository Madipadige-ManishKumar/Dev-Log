# dictionary is a collection of key-value pairs
# the Key Should be as it is .They are case sensitive 
mydict={
    "Fast":"In a Quick Manner ",
    "Living Thing ":"Humans,plants,animals",
    "Marks":[1,2,3] ,#list
    "Fast" :"Quick", # if we have same key then it is replced with recent update 
    "mydict1":{     # nested Dictinary  
         "Harry":"Coder",
         "Elon Musk":"Multi Talented"
    }
}
# printing the value of dictionary
print(mydict["Fast"])
print(mydict["Marks"])
print(mydict["mydict1"]["Elon Musk"])
# acessing the Value of dictionary
mydict["Marks"]=[45,78]
print(mydict["Marks"])
print(type(mydict))
print(list(mydict))
print(type(mydict))
print(mydict.values() )# gives the values of dictorionary 
print(mydict.items()) # give the value with key 
print(mydict)
Updatedi={
    "worng":"bsd",
    "osdhj":"sdjn"
}
print(mydict.items())
mydict.update(Updatedi)
print(mydict.items())
print(mydict.get("Fast1"))
print(mydict["Fast"])
# we use get method to get the data in disctionary 
'''
 What Is The Difference between get method and dictornary_name["key"]
is that when a key is not present in dictoinary then  dictornary_name["key"] it will throw the error 
where as get method print the none 
'''
# set
# The Set Is Collection No Repetative element
# set does not have index
# in set  you can  also give the different datatype 
a={1,2,3,4}# intilization of set 
# a={} this will create a empty dictionary but not empty set 
print(type(a))
a.add(7)
print(a)
# syntax to create an empty set 
B=set()
print(type(B))
print(B)
B.add(1)
B.add(2)
B.add(7)
B.add(3)
B.add(5)
B.add(6)
# B.add([4,5,6]) list can't be add in the set 
print(B)
# The Set Is Collection No Repetative element
c={11,11,11,12,12,12}
B.remove(1)
print(B)
print(B.pop())
print(B)
# B.remove(9) throws the error because the elemet is not present in set 
print(c)# it has only 11,12
print("The Union ",B.union(a))
print("The InterSection is ", B.intersection(a))