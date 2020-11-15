#armstrong num

n = 1634
order=len(str(n))
sum=0

temp = n
while (temp>0):
    ld=temp%10
    sum = sum+ld**order

    
    temp =temp//10

if n==sum:
    print("armstrong")
else:
    print("not")