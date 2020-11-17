n = "nitin"
m=len(n)
for i in range(len(n)//2):
    if n[i]!=n[m-1-i]:
        
        print("no")
        break
else:
    print("yes")





