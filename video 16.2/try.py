def howManyGames(p, d, m, s):
    l = []
    for i in range(s):
        y = (p - d*i)
        if y > m:
            l.append(y)
        elif m >= y > 0:
            h = s*[m]
            print(h)
            l.append(y)
    print(l)
    sm = 0
    ct =0       
    for i in l:
        sm += i
        
        if sm < s:
            ct += 1
            
            
    print(ct)
    return ct




print(howManyGames(16,2,1,9981))
#9917