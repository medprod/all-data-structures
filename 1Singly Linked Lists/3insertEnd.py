#Adding an Element at the end of linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head == None:
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
        newNode = Node(data) #creating a node
        if self.head is None: #new node will be the first node if linked list is empty
            self.head = newNode
        else:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = newNode
                
ll = LinkedList()
ll.addBegin(10)
ll.addBegin(40) 
ll.printList()
ll.addEnd(90)
ll.addEnd(100)
ll.addBegin(30) 
ll.printList()
ll.addEnd(55)
ll.printList()

#40 -->10 -->30 -->90 -->100 -->55 -->    
    




