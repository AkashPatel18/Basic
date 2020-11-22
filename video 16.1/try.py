'''
s = "akash patel.patel akash"
r="."
for i in r:
    s = s.replace(i,'\n')
print(s)
'''

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        return 10000
    elif y2>y1:
        return 0
    elif m1>m2:
        return (m1-m2)*500
    elif d1>d2:
        return (d1-d2)*15
    else:
        return 0

print(libraryFine(28,2,2015,15,4,2015))
