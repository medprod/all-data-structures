#adding an element in the beginning

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
                print(self.head.data)
                self.head = self.head.next 

    def addBegin(self, data):
        #creating a new individual node
        newNode = Node(data)
        #the reference of next node after the new node will be stored in the new node
        newNode.next = self.head
        #new node becomes the head
        self.head = newNode

ll = LinkedList()
ll.addBegin(10)
ll.addBegin(20) #adds before 10
ll.addBegin(40) #40, 20, 10
ll.printList()






                