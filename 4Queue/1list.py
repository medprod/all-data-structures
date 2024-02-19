queue = []
def push():
    if len(queue)==size:
        print("Queue is Full.")
    else:
        elem = input("Enter the Element: ")
        queue.append(elem)
        print(queue)

def pop():
    if not queue:
        print("Queue is Empty.")
    else:
        rem = queue.pop(0)
        print(queue)

size = int(input("Maximum Elements: "))
while True:
    print("Select the operation: 1=Enqueue, 2=Dequeue, 3=Quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter Valid Choice.")
