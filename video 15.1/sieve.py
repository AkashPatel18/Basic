n = int(input())
l1 = [0]*n
print(l1)
for i in range(2,n+1):
    #if l1[i]==0:
    for j in (i*i,n+1,i):
        l1[j]=1
    i += 1
for i in range(2,n+1):
     if l1[i]==0:
         print(i)         

