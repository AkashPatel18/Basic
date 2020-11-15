l1 = [1,2,0,7,2,0,2,2]
mx=-999999

for i in range(1,len(l1)):
    mx = max(mx,l1[i])
    print(mx)