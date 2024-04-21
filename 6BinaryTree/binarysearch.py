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
                
    def delete(self, value):
        if self.root is None:
            print("Tree is empty, has no elements")
        else:
            self.deleteNode(self.root, value)
                
    def deleteNode(self, node, value):
        if value < node.value:
            self.deleteNode(node.leftChild, value)
        elif value > node.value: 
            self.deleteNode(node.rightChild, value)
            #if value == node.value
        else:
            if node.leftChild is None:
                node = node.rightChild
            elif node.rightChild is None:
                node = node.leftChild
            else:
                node = self.successor(node)
                node = self.deleteNode(node, value)
                
        return node
                
    def successor(self, node):
        if node.rightChild:
            node = node.rightChild
            while node.leftChild:
                node = node.leftChild
                
        return node

    
    def inOrder(self, node, res):
        if node:
            self.inOrder(node.leftChild)
            print(node.value)
            self.inOrder(node.rightChild)
    
if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(6)
    
    
    
        

        
            
            
            
            
            