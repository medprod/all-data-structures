#Leetcode 1 - Two Sum Question
li = [2,7,11,15]

#2+7 = 9

def pairs(li, target):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == target:
                return i,j

print(pairs(li, 18))
            

