#finding the maximum product of 2 integers in an array where all elements are positive

arr = [1, 20, 40, 2, 5, 8, 9, 10]

def maxProduct(array):
    prod = 0
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i]*array[j] > prod:
                prod = array[i] * array[j]
    
    return prod

print(maxProduct(arr))
                

