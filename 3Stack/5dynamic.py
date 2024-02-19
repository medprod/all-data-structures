class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class dynamicStack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0 #Node top is null

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        print(self.head.data)

    def pop(self):
        if not self.head:
            print("Stack is Empty")
        else:
            self.head = self.head.next
        


    # def display(self):
    #     if not self.head:
    #         print("No data to display")
    #     else:
    #         print("Elements in the stack are: ")
    #         while self.head:
    #             print(self.head.data)
    #             self.head = self.head.next



ds = dynamicStack()
ds.push(5)
ds.push(6)
ds.pop()






    

    
