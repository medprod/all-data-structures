from LinkedList import LinkedList

def sumLists(ll1, ll2):
    p1 = ll1.head
    p2 = ll2.head
    carry = 0

    llres = LinkedList()

    while p1 or p2:
        result = carry
        if p1:
            result+=p1.value
            p1 = p1.next
        if p2:
            result+=p2.value
            p2 = p2.next
        
        llres.add(int(result%10))
        carry = result/10

    return llres

ll1 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)

ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)


print(sumLists(ll1, ll2))

