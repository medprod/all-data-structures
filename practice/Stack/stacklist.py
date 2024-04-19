#creating stack with list without size limit

class Stack:
    def __init__(self):
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

    def push(self, value):
        self.list.append(value)
        return "Element successfully inserted."
    
    def pop(self):
        if self.isEmpty():
            return "stack already empty."
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "stack empty."
        else:
            return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None

custom = Stack()
custom.push(1)
custom.push(4)
custom.push(2)
print(custom)
print(custom.peek())

custom.pop()
print(custom)
print(custom.isEmpty())

print(custom.peek())
    