row =10
n = row//2

for i in range(1,n+1):
    for j in range(1,2*n+1):
        if j>i and j<2*n+1-i:
            print("  ",end="")
        else:
            print("* ",end = "")
    print()

for i in range(n,0,-1):
    for j in range(2*n,0,-1):
        if j>i and j<2*n+1-i:
            print("  ",end="")
        else:
            print("* ",end = "")
    print()
        