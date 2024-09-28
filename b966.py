n=int(input())
data=[]
for i in range(n):
    s,t=map(int, input().split())
    data.append((s,t))
data.sort()
l=0
r=0
total=0
for s,t in data:
    if s<=r:
        r=max(r,t)
    else:
        total+=r-l
        l,r=s,t
total+=r-l
print(total)