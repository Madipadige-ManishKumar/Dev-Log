import numpy as np 
print(int(np.median([1,2,3,4])))
print((np.mean([1,2,3,4])))
my_array=np.genfromtxt("sample.txt",delimiter=",")
from  PIL import Image
# image processing 
image=Image.open("C:\\Programming_Files\\python-advanced\\my_numpy\\moltres.webp")
arr=np.array(image)
print(image)
f=open("sample.txt",encoding="UTF")
print(arr)
arr=np.array([1,2,3])
print(arr)
arr=np.append(arr,4)
print(arr)