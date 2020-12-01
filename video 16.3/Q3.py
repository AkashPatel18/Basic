

def hanoi(n,start  ,final, helper):
    if n==0:
        return
    hanoi(n-1,start,helper,final)
    print("move from", start, " to", final)
    hanoi(n-1,helper,final,start)

print(hanoi(3,'A','C','B'))