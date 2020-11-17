sent = "do orjkjk diee"

ans = 0
mx = 0

for i in sent:
    
    ans = ans+1

    if i ==" ":
        ans = 0
    mx = max(mx,ans)

long = max(sent.split())
      

print(mx,long)