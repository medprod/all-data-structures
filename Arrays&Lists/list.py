myList = [1,2,3,4,5]

myList[1] = 33

myList.insert(0,11)

myList.extend(['spam', 14, 5.5])

print(myList)
print(myList[2:-1])

myList[0:2] = ['x', 'y']
print(myList)

#pop(index)
myList.pop(1) #if no index provided, it will delete the last element

#remove(value)
myList.remove('x')
print(myList)