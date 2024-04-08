#given two lists, is one the permutation of another

li1 = ['a', 'b', 'c']
li2 = ['c', 'b', 'd']

def permutation(li1, li2):
    if len(li1) == len(li2):
        li1.sort()
        li2.sort()

    if li1 == li2:
        return "yes, permutation exists."
    else:
        return "no permutation."

print(permutation(li1, li2))