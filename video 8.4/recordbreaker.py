l = [1,2,0,7,2,0,2,6]
n = len(l)
mx = -1999999
ans = 0

for i in range(n):
    if l[i]>mx and l[i]>=l[i+1]:
        ans = ans +1
        mx = max(mx,l[i])


print(ans)
