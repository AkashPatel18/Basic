def insertionSort(list1):
    n = len(list1)
    for i in range(n):
        a = list1[i]
        while(list1[i-1]>a and i > 0):
            list1[i],list1[i-1]=list1[i-1],list1[i]
            i = i-1
    return list1

list1 = [12,45,23,51,19,8]
print("FINAL",insertionSort(list1))