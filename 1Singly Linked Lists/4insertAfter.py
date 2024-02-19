#adding element AFTER a given node

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head==None:
            print("Linked List is Empty")
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
        if self.head == None:
            self.head = newNode
        else:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = newNode

    def addAfter(self, data, x):
        while self.head is not None:
            #we are searching for x (the node before the node we're trying to add)
            if x == self.head.data: #come out of loop when we find x
                break
            else:
                self.head = self.head.next #else, increment to the next node and check if data==x

        if self.head is None:
            print("Node is not present in Linked List")
        else:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.next = newNode

ll = LinkedList()
ll.addBegin(20)
ll.addBegin(40)
ll.printList()
ll.addEnd(100)
ll.addAfter(200, 100)
ll.printList()


#40--> 20 -->100 -->200 -->


        

        



