l = list(map(int,input().split()))
key = 5
for i in range(len(l)):
    if key == l[i]:
        print(True)
        break
else:
    print(False)
        

