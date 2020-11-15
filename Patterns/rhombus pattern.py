n =5

for i in range(1,n+1):
    for j in range(1,2*n+1): 
        if j<n-i+1:
            print(" ",end=" ")
        elif j<2*n-i+1:
            print("*",end = " ") 
    print()