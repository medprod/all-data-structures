n = int(input("Enter the number of entries in the phonebook: "))
phoneBook = {}

for i in range(0,n):
    key, value = input().split()
    phoneBook[key] = value
    
for j in range(0,n):
    name = input("Enter a name to search: ")
    if name in phoneBook:
        print(name +'=' + phoneBook[name])
    else:
        print("Not found")