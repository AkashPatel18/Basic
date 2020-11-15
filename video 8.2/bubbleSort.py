def bubbleSort(list1):
    for i in range(len(list1)-1,0,-1):
        print(list1)
        for j in range(i):
            if list1[j]>list1[j+1]:
                temp = list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
                print(list1)
    return list1








list1 = [12,45,23,51,19,8]
print("FINAL",bubbleSort(list1))