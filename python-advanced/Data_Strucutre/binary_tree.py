class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
class binary_Tree:
    def __init__(self):
        self.root=None
    def head(self,data):
        new_Node=Node(data,None,None)
        self.root=new_Node
    def add(self,data):
        new_node=Node(data,None,None)
        temp=self.root
        while temp:
            if temp.data >data:
                if temp.left==None:
                    break
                temp=temp.left  
            elif temp.data<data:
                if temp.right ==None:
                    break
                temp=temp.right
        if temp.data > data:
            temp.left=new_node
        elif temp.data<data:
            temp.right=new_node
    def print(self):
        temp=self.root
        # while temp:
        #     print(f"{temp.left} : {temp.data}: {temp.right}")
        #     temp=temp.left
        # temp=self.root
        temp1=temp.left
        print(temp1.left.data,temp.left.data,temp.data,temp.right.data)
            
if __name__=="__main__":
    tree=binary_Tree()
    tree.head(10)
    tree.add(2)
    tree.add(11)
    tree.add(1)
    tree.print()