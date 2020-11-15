n = 5


for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j ==i:

            print("*",end = "")
        else:
            print(" ",end="")


for o in range(n,0,-1):
    for a in range(n,o+1,-1):
        if a==1 or a ==o:

            print("*",end = "")
        else:
            print(" ",end="")


    print()