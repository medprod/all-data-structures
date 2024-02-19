#creating a node with data and next in it
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    #creating an empty linked list
    def __init__(self):
        self.head = None

    #traverse through the linked list
    def printList(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

    #adding element in the beggining
    def addBeg(self, data):
        #create a new node
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    #adding element in the end
    def addEnd(self, data):
        #create a new node
        newNode = Node(data)
        #if linked list is empty, newNode is the only node in list so it is head
        if self.head is None:
            self.head = newNode
        else:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = newNode

    #adding element after given node
    def addAfter(self, data, x):
        while self.head is not None:
            #find the given node we're trying to add the newNode after of
            if x==self.head.data:
                break
            else:
                self.head = self.head.next

        #what is x is not even in linked list?
        if self.head is None:
            print("Node is not present in Linked List.")
        else:
            #create a new node
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.next = newNode

    #adding element before given node
    def addBefore(self, data, x):
        if self.head is None:
            print("Linked List is Empty.")
            return
        #if first element is the x we are looking for (adding before first node)
        if self.head.data == x:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return

        #adding element before the rest of the positions

        #find previous node first
        while self.head.next is not None:
            if self.head.next.data==x:
                break
            self.head = self.head.next

        #if x not even in linked list
        if self.head.next is None:
            print("Node not found.")
        else:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.next = newNode

    def deleteBeg(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head = self.head.next

ll = LinkedList()
ll.addEnd(50)
ll.addBeg(10)
ll.addAfter(20,10)
ll.addBefore(40,20)
ll.addBeg(70)
ll.deleteBeg() #deletes 70
ll.printList()
