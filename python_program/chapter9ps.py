f=open("sample.txt","r")
data=f.read();

data=data.replace("os","Operating System")
print(data)
f.close()
f=open("another.txt","w")
f.write(data)
f.close()