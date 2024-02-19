#creating a dictionary

engToTel = {"one": "okkati", "two": "rendu", "three": "mudu"}
print(engToTel)


#accessing an element
print(engToTel['one']) #put key value

#updating elements
myDict = {"name": "Edi", "age": 26}
myDict["age"] = 27
print(myDict)

#adding elements
myDict = {"name": "Edi", "age": 26}
myDict["address"] = "London"
print(myDict) #{'name': 'Edi', 'age': 26, 'address': 'London'}

#traversing
myDict = {"name": "Edi", "age": 26, "address": "London"}
def traverse(dict):
    for key in dict:
        print(key, dict[key])

print(traverse(myDict))

#searching for an element
def searchDict(dict, value):
    for key in dict:
        if dict[key]==value:
            return key, value
    return "value doesn't exist."

print(searchDict(myDict, 26))

#deleting element
# print(myDict.pop("name")) #Edi 

# print(myDict.popitem()) #random key value pair popped

del myDict['age']
print(myDict) #{'name': 'Edi', 'address': 'London'}

# print(myDict.clear()) #deletes all elements


