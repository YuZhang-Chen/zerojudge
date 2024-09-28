n=int(input())
s=input().split()
for x in range(n):
    num=[]
    for i in range(len(s)):
        s[i]=str(s[i])
        sum=0
        for j in range(len(s[i])):
            sum+=int(s[i][j])**(x+2)
        num.append(str(sum))
    aa=set(s)&set(num)
    s=list(set(s)-aa)

for i in range(len(s)):
    s[i]=int(s[i])
print(*sorted(s))