n=int(input())
s=list(map(int, input().split()))
t=int(input())
q=[t]
while len(q)>0:
    t=q.pop(0)
    boom=s[t]
    if boom==0:
        continue
    s[t]=0
    if boom==1:
        s[t]=0
    elif boom==2:
        if t-1>=0:
            q.append(t-1)
        if t+1<len(s):
            q.append(t+1)
    else:
        if t-boom>=0:
            q.append(t-boom)
        if t+boom<len(s):
            q.append(t+boom)
        if t-2*boom>=0:
            q.append(t-2*boom)
        if t+2*boom<len(s):
            q.append(t+2*boom)
print(*s)