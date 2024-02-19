def sumofdigits(n):
    assert int(n)==n, "Only integers."
    if n==0:
        return 0
    else:
        n = abs(n)
        return int(n%10) + sumofdigits(int(n/10))

print(sumofdigits(-113))

