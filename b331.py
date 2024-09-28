s=input().split('+')
for i in range(len(s)):
    s[i]=eval(s[i])
print(str(sum(s))[-4:])