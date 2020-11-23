def dec(n):
    if n == 0:
        return 0
    #return n,dec(n-1)
    dec(n-1)
    print(n)
    
print(dec(4))