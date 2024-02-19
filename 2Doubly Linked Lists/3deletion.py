class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def printFor(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

    def printRev(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            while self.head is not None:
                self.head = self.head.next
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.prev

    #pushing elements into an empty linked list
    def push(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
    
    #insert an element in the beginning 
    def addBeg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    #insert an element at the end 
    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.next is not None:
                self.head = n.next
            n.next = newNode
            newNode.prev = n

    def addAfter(self, x, data):
        if self.head is None:
            print("Linked List is empty.")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("Node not found.")
            else:
                newNode = Node(data)
                newNode.prev = n
                newNode.next = n.next
                if n.next is not None:
                    n.next.prev = newNode
                n.next = newNode

            #add before given element
     def addBefore(self, x, data):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                else:
                    n = n.next

            if n is None:
                ("Given Node is not present in DLL.")
            else:
                newNode = Node(data)
                newNode.next = n
                newNode.prev = n.prev
                
                if n.prev is not None:
                    n.prev.next = newNode
                else:
                    self.head = newNode
                n.prev = newNode


    #delete the first element 
    def delBeg(self):
        #no nodes in DLL
        if self.head is None:
            print("Doubly Linked List is empty.")
            return
        #DLL has only 1 node
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting that node.")
        else:
            self.head = self.head.next
            self.head.prev = None

    def delEnd(self):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting that node")
        else:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.prev.next = None

    def delBtwn(self, x):
        if self.head is None:
            print("Linked List is empty.")
            return
        #if only 1 node in linked list
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
            else:
                print("Node not found.")
            return

        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.data == x:
                n.prev.next = None
            else:
                ("Element not found")

              
dll = DLinkedList()
dll.push(10)
dll.addBeg(9)
dll.delEnd()
dll.printFor()
