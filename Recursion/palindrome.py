def isPalindrome(str):
    if len(str)<=1:
        return True
    elif str[0]!=str[-1]:
        return False
    else:
        return isPalindrome(str[1:-1])

print(isPalindrome("wow"))