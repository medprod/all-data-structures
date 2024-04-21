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
            node.leftChild = self.deleteNode(node.leftChild, value)
        elif value > node.value: 
            node.rightChild = self.deleteNode(node.rightChild, value)
            #if value == node.value
        else:
            if node.leftChild is None:
                node = node.rightChild
            elif node.rightChild is None:
                node = node.leftChild
            else:
                successor = self.successor(node.rightChild)
                node.value = successor.value
                node.rightChild = self.deleteNode(node.rightChild, successor.value)
               
        return node
                
    def successor(self, node):
        curr = node
        while curr.leftChild:
            curr = curr.leftChild
                
        return curr

    
    def inOrder(self, node, res):
        if node:
            self.inOrder(node.leftChild, res)
            print(node.value)
            self.inOrder(node.rightChild, res)
    
if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(14)
    bst.insert(4)
    bst.insert(25)
    bst.insert(5)
    bst.insert(6)
    
    print("Before deletion:", bst.inOrder(bst.root, []))
    bst.delete(10)
    print("After deletion:", bst.inOrder(bst.root, []))
    
    
    
        

        
            
            
            
            
            