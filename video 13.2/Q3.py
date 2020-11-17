str = "abcacbade"
mx= 0
for i in set(str):
    y = str.count(i)
    mx = max(y,mx)
print(mx)
