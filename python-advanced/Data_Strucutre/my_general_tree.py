# incomplete 

class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
class General_tree:
    def root_node(self,name):
        new_node=Node(name)
    def add_child(self,child_name):
        new_Node=Node(child_name)
        new_Node.parent=self
    def 
if __name__=='__main__':
    tree=General_tree()
    tree.root_node("Root")
    tree.add_child("Child1")
    pass