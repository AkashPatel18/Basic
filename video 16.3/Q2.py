s="pippxxppiixipi"

def pi(s):
    if (len(s))==0:
        return s
       
    elif s[0] == 'p' and s[1] == 'i':
        print("3.14",end="")
        pi(s[2:])
    else:
        print(s[0],end="")
        pi(s[1:])
print(pi(s))