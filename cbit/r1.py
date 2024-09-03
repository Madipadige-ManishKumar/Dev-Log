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
           return "empty"
        else:
            e=self.arr[self.top]
            self.top-=1
            return e

    def peek(self):
        if self.is_empty():
            return "empty"
        else:
            return self.arr[self.top]
class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=len(nums)
        s=my_stack(l)
        u=nums[::-1]
        for i in range(len(u)):
            s.push(u[i])
        if (l==1):
            if(k%2!=0):
                return -1
            else:
                return t[0]
        elif (l<k):
            s.pop()
            s.push(max(s.arr))
            return s.peek()
        else: 
            n=-1
            i=0
            lr=-1
            print("the len",len(nums))
            for i in range(k-1):
                print(i)
                print(s.arr[:s.top+1])
                if(n>lr):
                    lr=n
                    print("in ")
                n=s.pop()
            if(n>lr):
                lr=n

            s.push(lr)

        return s.peek()
k=int(input("Enter k operation"))
l=int(input("enter length "))
n=[]
for i in range(l):
    n1=int(input(f"Enter {i} th element"))
    n.append(n1)
n=n[::-1]

s=Solution()
print(s.maximumTop(n,k))