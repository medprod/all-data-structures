#single linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data #data of integers, numbers, or complex objects
        self.next = next #pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None #points to head of the linked list
    
    #printing function
    def print(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        #itr = iteration
        itr = self.head
        llstr = "" #a linked list string
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
        
    #method will insert element at beggining of linked list
    def insertBeginning(self, data):
        #Node Class above has two parameters - data & next
        node = Node(data, self.head) #data, self.head = next element is current head
        self.head = node #our head now is node
    
    #inserting element at the end
    def insertEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    #inserting a set of values 
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertEnd(data)

    #getting the length of the list
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    #removing an element given an index
    def removeElem(self, index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next #removing the head and pointing to next element
            return
        
        count = 0
        itr = self.head
        while itr:
            #previous element of the element we are trying to remove
            if count == index-1:
                itr.next = itr.next.next #points to the next element of the element we are removing

            itr = itr.next
            count+=1

    #inserting an element given an index
    def insertAt(self, index, data):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        #refer to the insertBeginning fxn to insert an element at index 0
        if index==0:
            self.insertBeginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count+=1

    def insertAfter(self, dataAfter, dataInsert):
        if self.head is None:
            return
        
        if self.head.data == dataAfter:
            self.head.next = Node(dataInsert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == dataAfter:
                node = Node(dataInsert, itr.next)
                break
            itr = itr.next

    def removeValue(self, data):
        if self.head is None:
            return
        
        if self.head.data==data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertBeginning(5)
    ll.insertBeginning(89 )
    ll.insertEnd(9)
    ll.insertEnd(90)
    ll.print()
    # #89-->5-->9-->90-->

    ll.insertValues(["banana", "mango", "apple"])
    ll.print()
    #banana-->mango-->apple-->

    print(ll.getLength()) 
    # #3

    ll.removeElem(2) #should remove apple
    ll.print()
    # #banana-->mango-->

    ll.insertAt(0,"figs")
    ll.print()
    # #figs-->banana-->mango-->

    ll.insertAt(2,"jackfruit")
    ll.print()
    # #figs-->banana-->jackfruit-->mango-->

    ll.insertAfter("banana", "cherry")
    ll.print()
    #banana-->cherry-->mango-->apple-->

    ll.removeValue("banana")
    ll.print()
    #cherry-->mango-->apple-->
