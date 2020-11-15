def selectionSort(list1):
    n = len(list1)
    print(n)
    for i in range(n):
        for j in range(i,n):
            if list1[j]<list1[i]:
                temp = list1[j]
                list1[j] = list1[i]
                list1[i] = temp
    return list1

list1 = [23,4,5,6,12,9,8]
print(selectionSort(list1))