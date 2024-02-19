#adding an element BEFORE given node

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head==None:
            print("Linked List is Empty.")
            return
        else:
            while self.head is not None:
                print(self.head.data, "-->", end="")
                self.head = self.head.next

    def addBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = newNode

    def addAfter(self, data, x):
        #Find X
        while self.head is not None:
            if self.head.data == x:
                break
            else:
                self.head = self.head.next

        if self.head is None:
            print("Node is not present in Linked List")
        else:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.next = NewNode
        
    def addBefore(self, data, x):
        if self.head is None:
            print("Linked List is Empty.")
            return
        #finding x
        if self.head.data == x:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return

        #goes to the previous node of x
        while self.head.next is not None:
            if self.head.next.data == x:
                break
            self.head = self.head.next 
        if self.head.next is None:
            print("Node is not found.")
        else:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.next = newNode

ll = LinkedList()
ll.addBegin(10)
ll.addBefore(40,100)
ll.printList()

#40 -->10 -->



        




    