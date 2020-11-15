

def pairsum(l1,key):
    low = 0
    high = n-1

    while(low<high):
        if (l1[low] + l1[high] == key):
            print(low,high,end=" ")
            return True
    
        elif (l1[low] + l1[high] < key):
            low = low + 1
        else:
            high = high -1
    else:
        return False
        
            











l1 = [2,3,7,11,14,16,20,21]
key = 70
n=len(l1)
print(pairsum(l1,key))

