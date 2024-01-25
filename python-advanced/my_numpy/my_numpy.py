import numpy as np 
#The BAsics 
a=np.array([1,2,3.0],dtype="int32")
# print(a)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b)
# print(a.ndim)
# print(b.shape)
# print(a.dtype)
# print(a.size)
# print("The Element at 0th index is ",a[0])
# print(b[0,1])
# print(b[0,:])
# print(np.zeros((2,3,4,5)))
# print(np.ones((2,3)))
# print(np.full((2,2),99))
# print(np.random.rand(1)[0])
# print(np.random.randint(1,size=(3,3)))
# a=np.array([1,2,3,4])

# print(a+2)

print(b[1:2,2:3])