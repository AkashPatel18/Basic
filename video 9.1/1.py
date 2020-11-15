C= int(input())

R= int(input())
a= 3
# one-liner logic to take input for rows and columns 
mat = [[int(input()) for x in range (C)] for y in range(R) ]
if mat[C][R] == a:
    print(True)

print(mat)