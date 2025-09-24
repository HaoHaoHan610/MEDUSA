class Node:
    def __init__(self,key):
        self.key = key
        self.height = 1
        self.right = None
        self.left = None



class Tree:
    def __init__(self):
        self.root = None
    
    def insertNode(self,r:Node, k:int):
        if r is  None: 
            return Node(key=k)
        elif k < r.key:
            r.left = self.insertNode(r.left,k)
        elif k > r.key:
            r.right = self.insertNode(r.right,k)
    
    def insert(self,k:int):
        self.root = self.insertNode(self.root,k)
    
    def inorder(self,r:Node):
        if r is not None:
            self.inorder(r.left)
            print(r.key , end=" ")
            self.inorder(r.right)

    def ALV(self):
        self.inorder(self.root)

    def getHeight(self,n:Node = None):
        if n is None:
            return 0
        return n.height
    
    def getBF(self,n:Node = None):
        if n is None:
            return 0
        return self.getHeight(n.left) - self.getHeight(n.right)
    

    def right_rotate(self,n:Node):
        





