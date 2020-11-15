l1 = [1,-4,3,2,1]
n = len(l1)

currsum = []
sum = 0

for i in range(n):
    sum = sum + l1[i]
    currsum.append(sum)

m= len(currsum)
maxsum = 0
for i in range(1,m):
    sum = 0
    final = []
    for j in range(m):
        sum = currsum[i]-currsum[j]
        final.append(sum)

print(max(final))





    
