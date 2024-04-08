# Day 1 - 11, 15, 10, 6 
# Day 2 - 10, 14, 11, 5 
# Day 3 - 12, 17, 12, 8 
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDarr = np.array([[11, 15, 10, 6 ], [10, 14, 11, 5 ], [12, 17, 12, 8 ], [15, 18, 14, 9] ])


newArr = np.insert(twoDarr, 0, [[1,2,3,4]], axis=1) #insert(which array, what column, elements, axis = 0 (for row) or 1(for column))
print(newArr)

newArr2 = np.delete(twoDarr, 1, axis=0)
print(newArr2)

newArr = np.append(twoDarr, [[1,2,3,4]], axis=1) (adds to the end of the matrix)

# Accessing elements in 2D array
print(newArr[0][1]) #arr[row][column]

#traversing 
def traverse(array):
    for i in range(0, len(array)):
        for j in range(0,len(array)):
            print(array[i][j])

# print(traverse(twoDarr))

#searching
def search(array, value):
    for i in range(0, len(array)):
        for j in range(0,len(array)):
            if array[i][j]==value:
                return str(i) + " " + str(j)

print(search(twoDarr, 15))