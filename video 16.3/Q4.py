s = "aaaaaaabbbbbbbbeeeeeeeeeeeccddddddd"
x=(set(s))
print(x)
ans=""
for i in x:
    ans += i
print(s)

def duplicate(s):
    if len(s)==0:
        return ""
    ch=s[0]
    ans=(s[1])
    if ch == ans[0]:
        return ans
    return duplicate(ch+ans)
print(duplicate(s))