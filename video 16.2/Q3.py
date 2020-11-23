def occ(arr,n,i,key):
    if i == n:
        return -1
    if arr[i]==key:
        return i



    return occ(arr,n,i+1,key)


arr = [2,36,73,4,5]
n = 5
i = 0
key =4 
print(occ(arr,n,i,key))
