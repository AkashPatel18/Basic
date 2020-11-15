l1 = [-1,4,-6,7,1,2,3,-4]
n=len(l1)
currsum = 0
maxsum = -19999
for i in range(n):
    currsum += l1[i]
    if currsum < 0:
        currsum=0
    maxsum = max(maxsum,currsum)
print(maxsum)