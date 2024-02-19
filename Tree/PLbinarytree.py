#Binary Tree using Python List

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "BT is full"
        self.customList[self.lastUsedIndex+1]= value
        self.lastUsedIndex += 1
        return "Value inserted."

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodeValue:
                return "value exists in BT"
        return "Not found"

    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrder(index*2) #leftChild formula
        self.preOrder(index*2 + 1) #rightChild formula

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrder(index*2)
        print(self.customList[index])
        self.inOrder(index*2 + 1)
    
    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrder(index*2)
        self.postOrder(index*2 + 1)
        print(self.customList[index])

    def levelOrder(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex==0:
            return "There is no node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i]==value:
                #replace last element with element you want to delete
                self.customList[i]= self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node successfully deleted."

    def deleteBT(self):
       self.customList = None
       return "The BT has been successfully deleted"

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))

# print(newBT.searchNode("Hot"))
# newBT.postOrder(1)

# newBT.levelOrder(1)

# print(newBT.deleteNode("Hot"))
# print(newBT.deleteBT())
