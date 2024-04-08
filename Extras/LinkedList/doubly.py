class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.prev = None
        node.next = None

    def insert(self, nodeValue, location):
        if self.head is None:
            print("Linked List is empty.")
        else:
            newNode = Node(nodeValue)
            #inserting at the beginning
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            #inserting at the end 
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1

                    newNode.next = tempNode.next
                    newNode.prev = tempNode
                    newNode.next.prev = newNode
                    tempNode.next = newNode

    def traverse(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    def reverseTraverse(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def search(self, nodeValue):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist"

    def delete(self, location):
        if self.head is None:
            print("Linked List empty.")
        else:
            if location==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location-1:
                    curNode = curNode.next
                    index +=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
    
    def delEntire(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

doubyLL = DLL()
doubyLL.create(5)
doubyLL.insert(0,0)
doubyLL.insert(2,-1)
doubyLL.insert(6,2)
print([node.value for node in doubyLL]) 
doubyLL.reverseTraverse()
print([node.value for node in doubyLL]) 
doubyLL.delEntire()
print([node.value for node in doubyLL]) 


                



            

            


                

                





