'''
i =0 
while i<10:
    print(i)
    i=i+1
'''
fri=["Mango","banana","Apple","pineapple"]
i=0;
#while loop
'''
while i<len(fri) :
    print(fri[i])
    i=i+1
    '''
# for loop 
for i in fri:
    print(i)
# range Funtion Is Used To Print The Scequence 
print("Range Function ")
for i in range(8):
    print(i)
for i in range(1,8):
    print(i)
# This Things Are not that Recommand 
# step size 
print("Step_Size")
for i in range (1,8,2):
    print(i)
# for with else
print("For With Else")
for i in range(8):
    print(i)
else:
    print("This Is Inside Else Of For ")
print("Break_Statement ")
# break Statement 
for i in range(8):
    print(i)
    if i==5 :
        break
else:
    print("This Is Inside Else Of For ")
print("Continue Statement ")
# continue statement 
for i in range(8):
    if i==5 :
        continue
    print(i)
# Pass_statement can be used with loop,if,function 
 i=4
if i>0:
    pass 
while i>6 :
    pass
def add(a,b):
    pass
print("We Have Used Pass_Statement")