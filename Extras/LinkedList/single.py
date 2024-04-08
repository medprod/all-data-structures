#creating individual nodes
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

#creating an empty linked list
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #insert in Linked List
    def insert(self, value, location):
        newNode = Node(value) #creates a node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            #adding node at the beginning of the linked list
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            
            #adding node at the end of linked list
            elif location==-1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            #adding element at the middle of linked list
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def search(self, nodeValue):
        if self.head is None:
            print("Linked List is empty")
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Value not in List."


    def delete(self, location):
        if self.head is None:
            print("Linked List is empty")
        else:
            #deleting first node from list
            if location==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            #deleting last node from list
            elif location==-1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        #traverse till the end of list
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
                    
            #deleting middle node from list
            else:
                tempNode = self.head
                index = 0 
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                newNode = tempNode.next
                tempNode.next = newNode.next

    #deleting entire linked list
    def delEntire(self):
        if self.head is None:
            print("Linked List empty.")
        else:
            self.head = None
            self.tail = None
                
singlyLL = SLinkedList()
singlyLL.insert(5,1)
singlyLL.insert(2,0) #0 = beginning of list
singlyLL.insert(3,1)
singlyLL.insert(4,-1) #end of list

print([node.value for node in singlyLL])
# singlyLL.delete(2)
singlyLL.delEntire()
print([node.value for node in singlyLL])




# singlyLL.traverse() 
# print(singlyLL.search(2))