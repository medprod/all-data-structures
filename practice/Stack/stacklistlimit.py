#creating stack with list with size limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            return "element cannot be inserted into stack"
        else:
            self.list.append(value)
            return "element successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty cannot pop"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None

custom = Stack(4)
custom.push(1)
custom.push(4)
custom.push(2)
custom.push(3)
print(custom.isFull())
print(custom)
print(custom.peek())

custom.pop()
print(custom)
print(custom.isEmpty())

print(custom.peek())
            
