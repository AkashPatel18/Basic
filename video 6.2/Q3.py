def factorial(n):
    if n ==0:
        print("1")
    elif n<0:
        print("fact is not posibble")
        
    if n == 1:
        return n
    else:

        return n*factorial(n-1)
n = int(input())

if n ==0:
    print("1")
elif n<0:
    print("np")
print(factorial(n))
