li = [1,2,3,4,5,6, 7, 8,9,10, 11, 12, 13, 14, 15, 17, 18, 19, 20]

#n = total number of integers
#sum of n integers = n(n+1)/2

def missingnum(li, n):
    sum1 = n*(n+1)/2#if it's 10 integers, n=10 (supposed to be sum)
    sum2 = 0
    for i in li:
        sum2 += i

    diff = sum1 - sum2
    print(diff)

missingnum(li, 20)


