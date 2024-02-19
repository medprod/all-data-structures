class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLL:
    def __init__(self):
        self.head = None

    #traverse forward
    def printFor(self, data):
        if self.head is None:
            print("Linked List is empty.")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

    #traverse backward
    def printRev(self, data):
        if self.head is None:
            print("Linked list is empty.")
        else:
            #reaching the last node
            while self.head is not None:
                self.head = self.head.next
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.prev




def printRev(self, data):
    if not self.head:
        print("Linked List is Empty")
        return
    else:
        #go to the last node in the list and make it head
        while self.head:
            self.head = self.head.next

        #now traverse from last to first
        while self.head:
            print(self.head.data)
            #make the previous element head 
            self.head = self.head.prev 

