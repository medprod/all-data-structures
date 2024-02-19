#Binary Tree using linked list
import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")

sprite = TreeNode("Sprite")
pepsi = TreeNode("Pepsi")

rightChild.leftChild = sprite
rightChild.rightChild = pepsi

newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)

def inOrder(rootNode):
    if not rootNode:
        return
    
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQ = queue.Queue()
        #to insert a root node into queue
        customQ.enqueue(rootNode)

        while not(customQ.isEmpty()):
            root = customQ.dequeue() 
            print(root.value.data)

            #if left child exists, enqueue the left child to customQ
            if(root.value.leftChild is not None):
                customQ.enqueue(root.value.leftChild)
            
            #if right child exists, enqueue the left child to customQ
            if(root.value.rightChild is not None):
                customQ.enqueue(root.value.rightChild)
            

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return "The Binary Tree does not exist"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()

            if root.value.data == nodeValue:
                return "Success"

            if(root.value.leftChild is not None):
                customQ.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQ.enqueue(root.value.rightChild)

        return "Node not in Binary Tree"

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Insertion Sucess"
            
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Insertion Sucess"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return "Binary Tree is empty."
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQ.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQ.enqueue(root.value.leftChild)

def deleteNode(rootNode, node):
    if not rootNode:
        return "BT not existing"

    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Node successfully deleted."

            if(root.value.leftChild is not None):
                customQ.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQ.enqueue(root.value.rightChild)
        return "Failed to delete"

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted" 




# preOrder(newBT)
# inOrder(newBT)

# levelOrder(newBT)
# print(searchNode(newBT, "Cola"))

# newNode = TreeNode("Cola")
# print(insertNode(newBT, newNode))

# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)

# deleteNode(newBT, 'Coffee')

deleteBT(newBT)
levelOrder(newBT)

