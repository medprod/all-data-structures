from array import *

arr1 = array('i', [1,2,3,4,5,6])

def searchInArr(array, value):
    for i in array:
        if i==value:
            return array.index(value)

    return "Element not in array."

print(searchInArr(arr1, 5)) #returns the index of the value if it exists