myDict = {"name": "Edi", "age": 26, "address": "London"}

#copy()
dict = myDict.copy()
print(dict)

#fromkeys()
newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

#get()
print(myDict.get('age', 27)) #26
print(myDict.get('city', 27)) #27
print(myDict.get('city')) #None


#items()

print(myDict.items()) #dict_items([('name', 'Edi'), ('age', 26), ('address', 'London')])

#keys() & values()
print(myDict.keys()) #dict_keys(['name', 'age', 'address'])
print(myDict.values())

#update()
new = {'a': 1, 'b': 2, 'c': 3}
myDict.update(new)
print(myDict)
#{'name': 'Edi', 'age': 26, 'address': 'London', 'a': 1, 'b': 2, 'c': 3}


