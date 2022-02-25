"""
from tkinter import *

'''
Theroy()
{
geometry method  . This method is used to set the dimension of the tkinter  window 
gemotry Manager in tkinter 
    1) Pack Manager
    2) grid Manager 
    3) Place manager
}
'''


def display():
    user=e1.get()
    pw=e2.get()
    print(user+" "+pw)
    
def display1():
    if(var.get()==1):
        print("Male")
    if (var1.get()==1):
        print("Female")
def display2():
    if (var11.get()==0):
        print("Male")
    else:
        print("Female")
win =Tk()
f1 = Frame(win,height=100,width=100,bg="yellow")
f1.pack()
win.geometry("300x300")
user=StringVar()
pw=StringVar()
Label(f1,text="User name ").grid(row=0,column=0)
e1=Entry(f1)
e1.grid(row=0,column=1)
Label(f1,text="Password").grid(row=1,column=0)
e2=Entry(f1)
e2.grid(row=1,column=1)


f2=Frame(win,height=100,width=100,padx=10,pady=10,bg="grey")
f2.pack()
var= IntVar()
var1=IntVar()

c1=Checkbutton(f2,text="C",variable=var,command=display1).grid(row=2,column=0)
c2=Checkbutton(f2,text="C++",variable=var1,command=display1).grid(row=2,column=1)
Button(win,text="Login",command=display).pack()

var11=StringVar()
r1=Radiobutton(win,text="male",variable=var11,command=display2,value=1).pack()
r2=Radiobutton(win,text="female",variable=var11,command=display2,value=2).pack()

f3=Frame(win,height=300,width=300)
f3.pack()
scroll=Scrollbar(f3)
l1 = Listbox(f3,yscrollcommand=scroll.set)
for i in range(70):
    l1.insert(END,str(i))
l1.pack()

scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=l1.yview)
mainloop()

"""




'''

The Event Hanling in python  in tkinter

from tkinter import *
win =Tk()


def harry(event):
    print(f"harry{event.x} , {event.y}")
def key(event):
    print(f"{event.char}")
b1 =Button(win,text="Press")
b1.pack()

b1.bind("<Button-1>",harry)
win.bind("<Button-1>",harry)
win.bind("<Key>",key)

mainloop()

'''


'''
Regular expression in python __?
'''


'''
File Operations


try:
    f=open("Chapter3.py",'r')
    data=f.read()
    f.close()
    f=open("another.txt",'w')
    f.write(data)
    f.close()
except Exception as e:
    print(e)

'''

from mysql.connector import *
try:
    conn = connect(
        host='localhost',
        user='root',
        password='cme123',
        database='db1'
    )
    print("Connect Done")
    cursor = conn.cursor()
    query="create table if not exists mytablr1(id int(3), name varchar(30))"
    cursor.execute(query)
    conn.commit()
    query="insert into mytablr1(id,name) values(3,'Asrit')"
    cursor.execute(query)   
    conn.commit()
    query="delete from mytablr1 where id=3"
    cursor.execute(query)
    conn.commit()
    query="select * from mytablr1"
    cursor.execute(query)
    re=cursor.fetchall()
    for i in re:
        print(i)
except Exception as e:
    print(e)