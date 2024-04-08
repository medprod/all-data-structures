class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #push
    def push(self, value):
        if self.isFull():
            return "cannot insert element stack is full"
        else:
            self.list.append(value)
            return "element successfully inserted"

    #pop
    def pop(self):
        if self.isEmpty():
            return "stack is empty cannot pop"
        else:
            self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "stack is empty no peek"
        else:
            return self.list[len(self.list)-1]

    #delete
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