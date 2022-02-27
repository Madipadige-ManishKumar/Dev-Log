# Numpy Provides the effcient storage 
#  it also provides better ways handling for processing 
# it is fast 
# it is easy to learn 
# Numpy uses relatively less memory to store data

import numpy  as np
# myarr=np.array([[3,2,4,90,45]],np.int8)
# # Int8 Indicates That the ebery element in array should maximum of 8 bytes 
# print(myarr[0,1])

# myarr[0,1]=7
# print(myarr[0,1])


# list_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(list_array[1,1])


# arr=np.array((34,23,23),dtype=object)
# print(arr)


# zeros=np.zeros((2,5))
# # # Creates The list of 2 rows and 5 columns of the zeros 
# # print(zeros)
# # rng=np.arange(15)

# # # Creates The List Of The 0 to  14 
# # print(rng)


# lspace=np.linspace(1,5,4)
# print(lspace)

# emp=np.empty((4,6))  # Create a list of random values of hte 4 rows and 6 column

# print(emp)

# emp_like=np.empty_like(lspace)

# print(emp_like)

# ide=np.identity(45)
# print(ide)
# print(ide.shape)

arr=np.arange(9)
arr=arr.reshape(3,3)
# print(arr)
# print(arr.reshape(3,33))


# print(arr.ravel())# Makes the array into 1d array 


print(arr.sum(axis=1))
print(arr.T)

print(arr.flat)

print(arr.ndim)

print(arr.size)

print(arr.nbytes)