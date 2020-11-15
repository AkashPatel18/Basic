#subArray

l1 = list(map(int,input().split()))
n = len(l1)
l2 = []
for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j+1):
            sum += l1[k]
            l2.append(sum)
        
print(max(l2))

l1 = [-1 ,4,7,2]
