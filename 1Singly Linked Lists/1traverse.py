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

ll = LinkedList()
ll.printList()