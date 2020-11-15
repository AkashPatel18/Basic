def binary(list1,key):
    left = 0
    right = len(list1) - 1
    #mid = (left + right)//2

    while(left <= right):
        mid = (left + right)//2
        

        if list1[mid]==key:
            return mid
        elif key < list1[mid]:
            right = mid -1
        else:
            left = mid+1


list1 = [1,2,3,4,5]
key = 5


print(binary(list1,key))