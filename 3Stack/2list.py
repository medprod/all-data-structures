stack = []
def push():
    if len(stack)==n:
        print("stack is full")
    else:
        elem = input("Enter the value of element: ")
        stack.append(elem)
        print(stack)

def popElem():
    if stack is None:
        print("stack is empty.")
    else:
        rem = stack.pop()
        print("Removed Element: ",rem)
        print(stack)

n = int(input("Maximum Elements: "))
while True:
    print("Select the operation: 1=Push, 2=Pop, 3=Quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice==2:
        popElem()
    elif choice==3:
        break
    else:
        print("Enter the correct operation!")
