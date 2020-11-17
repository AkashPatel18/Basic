mat =[[1,2,3],[4,5,6],[7,8,9]]
print(len(mat))
result=[[ 0 for i in range(3)] for j in range(3)]
for i in range(len(mat)):
    for j in range(len(mat)):
        result[i][j]=mat[j][i]
print(result)


