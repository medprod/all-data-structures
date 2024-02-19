
x = input()
y = input()
# print(type(x))
arr1 =  list(map(int, x.split(" "))) 
arr2 =  list(map(int, y.split(" "))) 
# print(arr)
# print(type(arr))


def mergeArrays(arr1, arr2):
    i, j = (0,0)
    m = len(arr1)
    n = len(arr2)
    
    ans = []
    
    while(i < m and j < n):
        if(arr1[i] < arr2[j]):
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
            
    if(i<m):
        while(i<m):
            ans.append(arr1[i])
            i+=1
    else:
        while(j<n):
            ans.append(arr2[j])
            j+=1
            
    print(ans)

def breakMerge(arr, start, mid, end):
    
    
    

    

# mergeArrays(arr1, arr2)
            