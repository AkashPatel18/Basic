def sorted(arr,n):

    if(n == 1):
        return True
    


    rest = sorted(arr,n-1)
    if (arr[0]<arr[1] and rest):
        return True
    
arr = [1,2,3,4,5]
n = 5
print(sorted(arr,n))
