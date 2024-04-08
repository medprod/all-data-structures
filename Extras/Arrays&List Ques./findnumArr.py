#finding a number in an array of integers

arr = [1, 2,3,44, 4, 5, 9, 10, 11, 2, 3, 55]
def find(arr, num):
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
        
print(find(arr, 44))