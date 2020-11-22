def raisedTO(n,p):
    if p == 0:
        return 1
    #pp = pow(n,p-1)
    return n*(n**(p-1))
print(raisedTO(2,3))
print(2**6)