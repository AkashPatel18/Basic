#reverse a num
n = int (input())

sum=0
while (n>0):
    ld=n%10
    sum=sum*10+ld
    n=n//10
print(sum)

