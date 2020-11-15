list =list(map(int,input().split()))
ans = []
sum = 0
for i in range(len(list)):
    sum = sum + list[i]
    ans.append(sum)
print(ans)