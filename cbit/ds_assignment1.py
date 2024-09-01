import array as arr
class my_stack:
    def __init__(self,l):
        self.l=l
        self.arr=arr.array("i",[0]*self.l)
        self.top=-1
    def is_full(self):
        if self.top==self.l-1:
            return True
        else:
            return False
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def push(self,e):
        if self.is_full():
            print("Stack is full")
        else:
            self.top+=1
            self.arr[self.top]=e
    def pop(self):
        if self.is_empty():
           print("under flow")
        else:
            e=self.arr[self.top]
            self.top-=1
            return e
    def peek1(self,n):
        if n:
            if self.is_empty():
                if n%2==0:
                    print(max(self.arr))
                else:
                    print(-1)
                exit()
            else:
                return self.arr[self.top]

    def peek(self):
        if self.is_empty():
            print(-1)
            exit()
        else:
            return self.arr[self.top]
if __name__ =="__main__":
    t=(input())
    t=t.split(" ")
    l=int(t[0])
    k=int(t[1])
    s=my_stack(l)
    t=input()
    t=t[::-1]
    t=(t.split())
    for i in range(len(t)):
        s.push(int(t[i]))
    if (l==1):
        if(k%2!=0):
            print(-1)
        else:
            print(t[0])
    else: 
        '''
        l =6 k =3 
          4 2 5   n =4 >  n1 =3  k =3
        '''
        n1=n=0
        for i in range(k):
            if(n>n1):
                s.pop()
                s.push(n)
                n=n1=0
                continue
            n=s.pop()
            print(f"The k-i ={int(k)-int(i)}")
            n1=s.peek1(k-i)
            print("The element is ",n,"   ",n1)
        print(s.peek())
        print(s.arr[:s.top+1])
        print(s.arr)