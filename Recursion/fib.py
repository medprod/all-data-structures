def fib(n):
    assert n>=0 and int(n)==n, "Cannot be negative or non-integers."
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))
