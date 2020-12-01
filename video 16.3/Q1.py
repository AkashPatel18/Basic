s= "bonod"

def strrec(s):
    if len(s)==0:
        return s
    else:
        return strrec(s[1:]) + s[0]

print(strrec(s))