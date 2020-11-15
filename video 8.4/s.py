l1 = [1,5,4,1,5,6,7,2]
sum = 3

n = len(l1)
for i in range(n):
    for j in range(i,n):
        if l1[i] + l1[j] == sum and i != j:

            print(i,j)
            


 