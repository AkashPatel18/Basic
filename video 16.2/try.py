import math as m
def encryption(s):
    ans = ""
    s="".join(s.split()) 
    print(s)
    n = len(s)
    print(s)
    
    l = m.sqrt(n)
    print(l)
    
    r = m.floor(l)
    print(r)
    
    c = m.ceil(l)
    print(c)
    
    