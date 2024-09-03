#User function Template for python3
class stack:
    def __init__(self, l):
        self.arr = [0] * l
        self.f = -1
        self.r=-1
        self.l = l

    def enqueue(self, n):
        if self.top == self.l:
            raise Exception("Overflow")
        else:
            if(self.f==self.r==-1):
            	self.f=self.r=0
				self.arr[self.r] = n


    def dequeue(self):
        if self.f == -1:
            raise Exception("Underflow")
        else:
            n = self.arr[self.f]
            self.f += 1
            return n

    def peek(self):
        if self.f == -1:
            return False
        else:
            return self.arr[self.f:self.r+1]

if __name__=="__main__":
    exp=input("Enter the input")
    s=stack(len(exp))
    my_dict = {
            '^': 3,
            '*': 2,
            '/': 3,
            '%': 4,
            '+': 5,
            '-': 6
    }
    for i in range(len(exp)):
        if exp[i].isalnum():
            s.push(int(exp[i]))
        elif exp[i] in my_dict:
            b = s.pop()
            a = s.pop()
            s.push(my_op(a,b,exp[i]))
        print(s.peek())
        '''
        ab/
        '''