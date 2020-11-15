def check(lst):
    last = lst[0]
    for num in lst[1:]:
        if num == last:
            return True
        last = num
    return False


lst = [1, 2, 3, 4, 5, 5, 6]
print (check(lst)) #Prints True