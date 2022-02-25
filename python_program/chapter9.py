# files 
# type Of File 
'''
With Statement is Best Way To Open it will automatically close the file
text file 
binary file (binary file is secure )
 The Default Mode Is Read Mode i.e 'r' ,'w'
We have Different Modes 
Like 
Open("File Name","mode") like r
Read
Write
Append 
'''

# opening and reading a file 
# f=open("sample.txt","r")
# data=f.read() read full data 
 # we can also keep the how many charcter to read like 
# data=f.read(5) # read the specified charcter   This statement will read the 5 charcter 
# print(f.readline())#read a single line

# writing into a file
'''
data=f.read()
f.close()
f=open("another.txt","w")
f.write(data)
f.close
f=open("another.txt","a")
f.write("print('This Program Is Written By 21001-cs-007')")
'''
# With Statement 
with open("another.txt","") as f:
    a=f.read()
print(a)