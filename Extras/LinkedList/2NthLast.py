#Find the nth to last element of a singly linked list

from LinkedList import LinkedList

def nthToLast(ll, n):
    p1 = ll.head
    p2 = ll.head

    for i in range(n):
        if p2 is None:
            return 
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1


customLL = LinkedList()
customLL.generate(10, 0, 99) #generating a random linked list of 10 digits ranging from 0 to 99
print(customLL)

print(nthToLast(customLL, 4))
