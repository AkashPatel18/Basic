n = 10   


def b2d(n):
    x=0
    ans = 0

    while(n>0):
        y=n%10


        ans = ans+ 8**x *y 
        x=x+1
        n=n//10

    return ans
print(b2d(n))


