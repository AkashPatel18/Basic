import math as m
n = 23
flag =0
for i in range(2,int(m.sqrt(n))):
    if n%i==0:
        print( n ,"is non prime")
        flag=1
        break
if flag==0:
    print("prime")