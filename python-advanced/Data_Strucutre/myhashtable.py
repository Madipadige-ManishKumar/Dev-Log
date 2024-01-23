#Channing  in hash table 
class Node:
    def __init__(self,key,value,next):
        self.key=key
        self.value=value
        self.next=next
class hash_table:
    def hash_function(self,key):
        sum=0
        for i in key:
            sum+=int(ord(i))
            print("ord(i)",ord(i))
        sum %=10

        print(sum)
        return sum
    def __init__ (self):
        self.memory=[None for i in range(100)]
    def __setitem__(self,key,value):
        new_node=Node(key,value,None)
        i=int(self.hash_function(key)-1)
        if self.memory[i] ==None:
            self.memory[i]=new_node
        else:
            temp=self.memory[i]
            while temp:
                if temp.next==None:
                    temp.next=new_node
                    break
                temp=temp.next
            

    def __getitem__(self,key):

        i=int(self.hash_function(key)-1)
        if self.memory[i]==None:
            raise Exception("Invalid key given")
        temp=self.memory[i]
        l=[]
        while temp:
            if key== temp.key:
                return temp.value
            temp=temp.next
    def print(self):
        print(self.memory)
ht=hash_table()
ht["march 6"]=120
ht["march 17"]=320
print(ht["march 6"])
print("hello")
print(ht.hash_function("mar 6"))
