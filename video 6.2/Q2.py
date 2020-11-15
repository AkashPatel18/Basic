


def fibonaci(t1,t2,n):
    t1 = 0
    t2 = 1
    
    for i in range(1,n+1):
        print(t1)
        nextTerm = t1 + t2
        t1 = t2
        t2 = nextTerm
        
    
   



print(fibonaci(0,1,9))
