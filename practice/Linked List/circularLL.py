class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def create(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node

    def insert(self, value, location):
        if self.head is None:
            return "Linked List is empty."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                #links the last node to the first node
                self.tail.next = newNode
            #adding node at the end of list
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    
    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    #searching
    def search(self, nodeValue):
        if self.head is None:
            print("Linked List is empty")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "Node does not exist in CLL."

    #delete
    def delete(self, location):
        if self.head is None:
            print("Linked List is empty")
        else:
            if location==0:
                #if only 1 element exists
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                #if only 1 element exists
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1

                nextNode = tempNode.next
                tempNode.next = nextNode.next

    #delete entire cll
    def delEntire(self):
        self.head = None
        self.tail.next = None
        self.tail = None
            

circularLL = CLL()
circularLL.create(1)
circularLL.insert(0,0)
circularLL.insert(2,-1) #0 = beginning of list
circularLL.insert(3,-1)
circularLL.insert(2,2) #end of list

circularLL.delete(2)


print([node.value for node in circularLL])
circularLL.traverse()


print(circularLL.search(2))
circularLL.delete(3)
print([node.value for node in circularLL])

