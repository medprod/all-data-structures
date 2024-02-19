
#concat
list1 = [1,2,3]
list2 = [4,5,6]
c = list1 + list2
print(c) #[1, 2, 3, 4, 5, 6]

a = [0]
a = a*4
print(a) #[0, 0, 0, 0]

a = [0,1]
a = a*4
print(a) #[0, 1, 0, 1, 0, 1, 0, 1]

a = 'spam spam spam'
b = a.split()
print(b) #['spam', 'spam', 'spam']

a = 'spam1-spam1-spam1'
b = a.split('-')
print(b)
print('-'.join(b))

a = [3,7, 1, 4, 2, 0]
print(sorted(a))
sorted(a)
print(a)

