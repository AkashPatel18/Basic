l = list(map(int,input().split()))
extra = int(input())
output = []

maxoflist= max(l)

for i in range(len(l)):
    if l[i]+extra < maxoflist:
        output.append("false")
    else:
        output.append("true")
print(output)