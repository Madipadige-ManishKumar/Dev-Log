# lambda Method 

# method One To Create Function (Smaller)
# def func(a):
    # return a+5
# Method 2   Using The Lambda Function 
# func=lambda a :a+5
# x=566
# print(func(x))


# Join Method 
# l=["Monitor","Mouse","Keyboard","Cpu"]
# sentence=",".join(l)
# print(sentence)

# Format Method 

# name="Manish"
# channel ="I Can "
# a="This Is {}   and his channel {}".format(name,channel)
# print(a)
# # You Can Also Change The Order By Using The Index 
# a="This Is {1}   and his channel {0}".format(name,channel)
# print(a)

#Map Function

# square=lambda a:a*a
# l=[1,2,3]
# print(list(map(square,l)))
# # fliter  it will create a list for exsting list if the function return true 
# print(list(filter(square,l)))

from functools import reduce
sum =lambda  a:a+a
l=[1,2,3,4,5]
val = reduce(sum,l)
print(val) 
