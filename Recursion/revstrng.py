def reverse(str):
    if len(str)<=1:
        return str
    return str[len(str)-1] + reverse(str[0:len(str)-1])

print(reverse("HELLO"))