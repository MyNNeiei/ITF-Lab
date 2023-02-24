class BSTNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

class BST :
    def __init__(self) :
        self.root = None
    def is_empty(self) :
        if self.root == None:
            return True
        else:
            return False
    def preorder(self, root):
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)
    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")
    def traverse(self):
        self.preorder(self.root)
        print()
        self.inorder(self.root)
        print()
        self.postorder(self.root)
        print()
        return
    def findMin(self):
        return
    def findMax(self):
        return
    def insert(self, data):
        pNew = BSTNode(data)
        if self.is_empty():
            self.root = pNew
        else:
            start = self.root
            while True:
                if data < start.data:
                    if start.left == None:
                        start.left = BSTNode(data)
                        break
                    else:
                        start = start.left
                elif data > start.data:
                    if start.right == None:
                        start.right = BSTNode(data)
                        break
                    else:
                        start = start.right

myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.traverse()
