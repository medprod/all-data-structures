myList = [1,2,3,45, 67, 90]

def search(list, value):
    for i in list:
        if i==value:
            return list.index(value)

    return "Not in List."

print(search(myList, 90))
