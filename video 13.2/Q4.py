str = "asaaaaaaaaaaaaasssssdssssss"

ans=str[0]
for i in range(1,len(str)):
    if str[i] != str[i-1]:
        ans = ans + str[i]
print(ans)



