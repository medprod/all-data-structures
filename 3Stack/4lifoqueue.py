import queue

stack = queue.LifoQueue(3)

def push():
    elem = input("Enter the element: ")
    stack.put(elem)
    print("Added Element: ",elem)
    print(stack)

def popElem():
    if not stack:
        print("stack is empty")
    else:
        rem = stack.get()
        print("Removed Element: ",rem)
        print(stack)

while True:
    print("Select the operation: 1=Push, 2=Pop, 3=Quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        popElem()
    elif choice == 3:
        break
    else:
        print("Invalid Choice.")