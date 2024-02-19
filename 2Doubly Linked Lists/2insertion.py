class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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
            temp = self.head
            newNode.next = temp
            temp.prev = newNode
            temp = newNode

    #insert an element at the end 
    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

    #add after given element
    def addAfter(self, data):
        if self.head is None:
            print("Linked List is Empty.")
        else:
            temp = self.head
            while self.head is not None:
                if x==temp.data:
                    break
                temp = temp.next
            if temp is None:
                print("Given Node is not present in DLL.")
            else:
                newNode = Node(data)
                temp.prev = self.head
                temp.next = self.head.next
                #if inserting element not after last node
                if temp.next is not None:
                    temp.next.prev = newNode
                temp.next = newNode
    
     #add before given element
     def addBefore(self, data):
        if self.head is None:
            print("Linked List is empty.")
        else:
            temp = self.head
            while temp is not None:
                if x == temp.data:
                    break
                else:
                    temp = temp.next

            if temp is None:
                ("Given Node is not present in DLL.")
            else:
                newNode = Node(data)
                newNode.next = temp
                newNode.prev = temp.prev
                
                if temp.prev is not None:
                    temp.prev.next = newNode
                else:
                    self.head = newNode
                temp.prev = newNode


        
        




                



dll = DLinkedList()
dll.push(10)
dll.addEnd(50)
dll.addBeg(90)
dll.addAfter(40, 10)
dll.printFor()


    



