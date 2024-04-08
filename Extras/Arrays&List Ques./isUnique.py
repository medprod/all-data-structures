#implement an algorithm to see if a list has all unqiue characters

li = [1, 2, 44, 7, 8, 9, 10, 90, 22, 235, 33]

temp = []

def isUnique(li):
    for i in li:
        if i not in temp:
            temp.append(i)

    if li == temp:
        return "all unique elements"
    else:
        return "some duplicate values"

print(isUnique(li))
        
