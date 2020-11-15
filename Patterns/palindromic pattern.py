n =5


for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end = " ")
    for k in range(i,0,-1):
        print('*',end=" ")
    for l in range(2,i+1):
        print("*",end=" ")
    print()
    #palindrom break
#star pattern continue
for i in range(1,n+1):
    for j in range(0,i):
        print(" ",end = " ")
    for k in range(i,n):
        print('*',end=" ")
    for l in range(2,n-i+1):
        print("*",end=" ")
    print()
    