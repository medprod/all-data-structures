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

    def create(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode


    def insert(self, value, location):
        if self.head is None:
            print("Empty")
        else:
            newNode = Node(value)
            if location==0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
            elif location==-1:
                newNode.prev = self.tail
                self.tail.next = newNode
                newNode.next = self.head
                self.head.prev = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode
                nextNode.prev = newNode
                newNode.prev = tempNode
    
    def traverse(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail.next:
                    break
                node = node.next


    def revtraverse(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.tail.next:
                    break
                node = node.next

    
    def search(self, nodeValue):
        if self.head is None:
            print("Linked List is empty.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    print(node.value)
                tempNode = tempNode.next
            return "not found."
    
    def delete(self, location):
        if self.head is None:
            print("Linked List is empty.")
        else:
            if location==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.prev = None
                    self.tail.next = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.prev = None
                    self.tail.next = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode
    
    def delEntire(self):
        if self.head is None:
            print("Linked List is empty.")
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
circularDLL.delete(1)
print([node.value for node in circularDLL])
