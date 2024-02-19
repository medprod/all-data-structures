#Given a Singly Linked List, find the middle node. 
#If there are an even number of nodes, then there will be two middle nodes and 
#function should return second middle node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #empty linked list
    def __init__(self):
        self.head = None

    #adding elements to empty linked list
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        while self.head:
            print(str(self.head.data) + "->", end = "")
            self.head = self.head.next
        print("NULL")

    #printing middle element
    def midElem(self):
        count = 0
        mid = self.head

        #traverses through elements and counts until last element
        while self.head is not None:
            count+=1
            self.head = self.head.next
        i = 1
        while(i<count/2):
            mid= mid.next
            i += 1
        print("The middle element is: ", mid.data)
        print(count)


ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(50)
ll.push(60)
ll.midElem()






