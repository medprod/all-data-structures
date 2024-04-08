
# arr = [1,2,3,4,3,9,3]
# count = 0

# for i in range(0,len(arr)):
#     if arr[i] == 3:
#         count +=1 

# print(count)



from array import *
arr = array('i', [1,3,5,7,9])
arr.append(11)
print(arr)

arr.reverse()
print(arr)

print(len(arr))

arr.extend(arr)
print(arr)

# array('i', [1, 3, 5, 7, 9, 11])
# array('i', [11, 9, 7, 5, 3, 1])
# 6
# array('i', [11, 9, 7, 5, 3, 1, 11, 9, 7, 5, 3, 1])


