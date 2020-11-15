l1 = list(map(int,input().split()))
n = len(l1)

for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = sum + l1[j]
        print(sum)
