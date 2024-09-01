class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
class ll:
    def __init__(self) :
        self.head=None
    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def insert_at_mid(self,data,p):
        c=0
        temp=self.head
        while temp.next:
            c+=1
            if(c==p):
                break
            else:
                temp=temp.next
        new_node=Node(data)
        t=temp.next
        temp.next=new_node
        new_node.next=t
        print(temp.next.data,"is the data")
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head=self.head.next
    def delete_at_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delete_at_mid(self,p):
        temp=self.head
        c=0
        while temp.next:
            if(c==p):
                temp.next=temp.next.next
                break
            else:
                temp=temp.next
            c+=1
if __name__=="__main__":
    l=ll()
    l.insert_at_start(1)
    l.insert_at_start(2)
    l.insert_at_start(3)
    l.insert_at_end(4)
    l.insert_at_mid(5,1)
    
    temp=l.head
    print("After inserting at start and before deleting")
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
    print()
    l.delete_at_start()
    l.delete_at_end()
    temp=l.head
    print("After deleting")
    while temp:
        print(temp.data,end=" ")
        temp=temp.next
    print()