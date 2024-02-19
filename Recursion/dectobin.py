def dectobin(n):
    assert int(n)==n, "Integer only."
    if n==0:
        return 0
    else:
        return n%2 + 10*dectobin(int(n/2))

print(dectobin(10))