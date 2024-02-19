import queue

q = queue.Queue(maxsize=5)

def push():
    full = q.full()
    if full:
        print("Queue is Full.")
    else:
        elem = int(input("Enter the Element: "))
        q.put(elem)
        print("Added Element: ",elem)
        print("Size: ", q.qsize())

def pop():
    empty = q.empty()
    if empty:
        print("Queue is Empty.")
    else:
        rem = q.get()
        print("Removed Element: ",rem)
        print("Size: ", q.qsize())

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