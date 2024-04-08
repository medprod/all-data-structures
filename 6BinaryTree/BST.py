#Binary Search Tree

import QueueLinkedList as queue #for level order traversal
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "Node has been successfully inserted."

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
        customQ.enqueue(rootNode)

        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found.")
    elif nodeValue < rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if nodeValue == rootNode.rightChild.data:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

def minValue(bstNode):
    current = bstNode
    #because minimum values are not the left side
    while(current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        #if we have only 1 child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BST has been successfully deleted."


newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
# print(newBST.data)
# print(newBST.leftChild.data)

# inOrder(newBST)

# searchNode(newBST, 100)
# deleteNode(newBST, 100)
# deleteBST(newBST)
levelOrder(newBST)