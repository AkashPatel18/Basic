#n1 = int(input())
n2 = int(input())

for i in range(2,n2):
    for j in range(2,i):
        if i%j==0:
            
            break
    else:
        print(i)
