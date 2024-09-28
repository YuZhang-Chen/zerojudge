input()
s=list(map(int, input().split()))
cost=0
for i in range(len(s)):
    if s[i]==0:
        if i==0:
            cost+=s[i+1]
        elif i==len(s)-1:
            cost+=s[i-1]
        else:
            cost+=min(s[i-1],s[i+1])
print(cost)