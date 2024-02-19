tup = ('a', 'b','c', 'd', 'e')

newtup = tuple('abcde')
print(newtup)

print(tup + newtup) #('a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e')

print(tup*4) #('a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e')

print('d' in tup) #True

print(newtup.count('d')) #1

print(tup.index('a')) #0

#min, max, len


print(tuple([1,2,3,4])) #list to tupe (1, 2, 3, 4)

#we can reassign a tuple but not change single elements
tup1 = 1,2,3,4,5

tup1 = 7,8,9,0
print(tup1)

init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)