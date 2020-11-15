

def spiral(m,n,a):
    k =0
    l=0

    while (k<m and l <n):   

        for i in range(l,n):
            print(a[k][i], end=" ")
        
        k = k+1
        

        for i in range(k,m):
            print(a[i][n-1],end =" ")

        n = n-1

        for i in range(n-1,l,-1):
            print(a[k][i],end=" ")
        m = m-1

        for i in range(m,k,-1):
            print(a[i][k],end=" ")

        l =l-1

a=[[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

r=3
c=6

spiral(r,c,a)

