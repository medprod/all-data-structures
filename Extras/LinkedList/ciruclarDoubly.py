class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def create(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next =  newNode

    def insert(self, value, location):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            newNode = Node(value)
            if location==0:
                newNode.next = self.head
                newNode.prev = self.tail #bc its circular
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traverse(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
    
    def revTraverse(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def search(self, nodeValue):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist."
                tempNode = tempNode.next

    def delete(self, location):
        if self.head is None:
            print("Linked List empty.")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location==-1:
                if self.head==self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head
                index = 0
                while index < location-1:
                    curNode = curNode.next
                    index +=1
                
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
    
    def delEntire(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

circularDLL = CDLL()
circularDLL.create(5)
circularDLL.insert(0,0)
circularDLL.insert(1,-1)
circularDLL.insert(2,2)
print([node.value for node in circularDLL])
circularDLL.delete(7)
print([node.value for node in circularDLL])




