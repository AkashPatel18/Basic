n =20

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end ="")
    for k in range(1,i):
        print(k,end =" ")
    print()