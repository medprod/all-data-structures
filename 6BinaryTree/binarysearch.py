class Node(object):
    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None
        
class BST(object):
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)
        
    def insertNode(self, node, value):
        if value <= node.value:
            if node.leftChild is None:
                node.leftChild = Node(value)
            else:
                self.insertNode(node.leftChild, value)
        else:
            if node.rightChild is None:
                node.rightChild = Node(value)
            else:
                self.insertNode(node.rightChild, value)
                
    
    def inOrder(self, node, res):
        if node:
            self.inOrder(node.leftChild, res)
            res.append(node.value)
            self.inOrder(node.rightChild, res)
        
                
    def print(self):
        res = []
        self.inOrder(self.root, res)
        print(res)
        
    
if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(6)
    
    bst.print()
    
        

        
            
            
            
            
            