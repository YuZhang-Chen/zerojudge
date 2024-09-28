n=int(input())
s=sorted(list(map(int, input().split())))
ans=0
while len(s)>1:
    a=s.pop(0)
    b=s.pop(0)
    ans+=a+b
    s.append(a+b)
    s=sorted(s)
print(ans)