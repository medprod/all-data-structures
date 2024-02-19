#removing duplicates from unsorted list

from LinkedList import LinkedList

#approach 1
def removeDups(ll):
    if ll.head is None:
        return 
    else:
        currNode = ll.head
        tempSet = set([currNode.value])
        while currNode.next:
            if currNode.next in tempSet:
                currNode.next = currNode.next.next
            else:
                tempSet.add(currNode.next.value)
        return ll

#approach 2
def removeDups2(ll):
    if ll.head is None:
        return
    
    currNode = ll.head
    while currNode:
        runner = currNode
        while runner.next:
            if runner.next.value==currNode.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currNode = currNode.next
    return ll.head


customLL = LinkedList()
customLL.generate(10, 0, 99) #generating a random linked list of 10 digits ranging from 0 to 99
print(customLL)

removeDups(customLL)
print(customLL)

# removeDups2(customLL)
# print(customLL)
