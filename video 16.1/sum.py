def sum(n):
    if n==0:
        return 0
    ps = sum(n-1)
    return n + ps

print(sum(5))