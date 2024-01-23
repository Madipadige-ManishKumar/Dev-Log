class Node:
    def __init__(self,data,next) :
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    # insert 
    def insert_first(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    def insert_mid(self,index,data):
        if index<0 or index>int(self.leng()):
            raise  Exception("Invalid Index has given")
        else:
            temp=self.head
            count=0
            while temp:
                count+=1
                if count==index:
                    new_node=Node(data,temp.next)
                    temp.next=new_node
                    break
                temp=temp.next
    def insert_end(self,data):
        new_node=Node(data,None)
        temp=self.head
        while temp:
            if temp.next==None:
                temp.next=new_node
                break    
            temp=temp.next
    def insert_after_value(self,val,data):
        new_node=Node(data,None)
        temp=self.head
        while temp:
            if temp.data == val:
                new_node.next=temp.next
                temp.next=new_node
                break
            temp=temp.next
    #delete 
    def delete_first(self):
        if  self.head==None:
            raise Exception("List is Empty")
        else:
            temp=self.head
            del self.head
            self.head=temp.next
            del temp
    def delete_end(self):
        temp=self.head
        while temp:
            if temp.next.next==None:
                del temp.next.next
                temp.next=None
                break
            temp=temp.next
    def delete_before_value(self,val):    
        if self.leng()<2:
            raise  Exception("Only one value")
            return
        elif self.leng()==2:
            print("length ==2")
            temp=self.head
            temp1=temp.next
            if temp.data==val:
                raise Exception("It is The first Elelment no element before ")
            elif temp1.data==val:
                self.head=temp1
                del temp
        elif self.leng()>=3:
            print(f"The length is {self.leng()}")
            temp=self.head
            temp1=temp.next
            temp2=temp1.next
            if temp.data==val:
                raise Exception("It is Starting element")
            elif  temp1.data==val:
                temp.next=temp2
                del temp1
            elif temp2.data==val:
                temp.next=temp2
                del temp1
            else:
                while temp2:
                    if temp2.data==val:
                        temp.next=temp2
                        del temp1
                        return
                    temp=temp.next
                    temp1=temp1.next
                    temp2=temp2.next
    #print 
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
    
	# length 
    def leng(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
    def sorting(self):
        pass


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_first(1) 
    ll.insert_first(2)
    ll.insert_end(3)
    ll.insert_end(7)
    ll.insert_mid(4,4)
    ll.insert_after_value(1,5)
    ll.insert_mid(4,6)
    # ll.delete_end()
    ll.delete_before_value(2)
    ll.print()
    