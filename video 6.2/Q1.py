import math

def isprime(start,end):
    for i in range(start,end+1):
        for j in range(2,int(math.sqrt(i))):
            if i%j==0:
                
                break
            else:
                print(i)

print(isprime(11,19))

