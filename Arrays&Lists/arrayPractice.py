from array import *

#creating array
arr = array('i', [1,2,3,4,5,6])

#traversing array
for i in range(0,len(arr)):
    print(arr[i])

#accessing individual elements through indexes
print(arr[2]) #3

#append() = only inserts elements at the end of the array
arr.append(8)
print(arr)

#insert() = inserts anywhere
arr.insert(4, 1) #insert(index, value)
print(arr)

#extend() 
arr2 = array('i', [10, 11, 12])
arr.extend(arr2)
print(arr)

#remove(value)
arr.remove(4)
print(arr)

#fromlist() - add elements from list to array
tempList = [20, 21, 22]
arr.fromlist(tempList)
print(arr)

#pop() - removes last element
arr.pop()
print(arr)

#index() - returns index of any given value
print(arr.index(5))

#tolist()
print(arr.tolist())

#slicing elements from array
print(arr[1:-1])




