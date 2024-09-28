data1=[]
data2=[]
mx=0
n, m=map(int, input().split())
for i in range(n):
    a, b=map(int, input().split())
    mx=max(a, b, mx)
    data1.append((a, b))

for i in range(m):
    a, b=map(int, input().split())
    mx=max(a, b, mx)
    data2.append((a, b))

d=int(input())
lst1=[0]*(mx+1)
lst2=[0]*(mx+1)

for a, b in data1:
    for i in range(a, b):
        lst1[i]=1

for a, b in data2:
    for i in range(a, b):
        lst2[i]=1

for i in range(mx+1):
    t=set(lst1[i:(i+d)])
    if lst1[i:(i+d)]==lst2[i:(i+d)] and len(t)==1 and list(t)[0]==1:
        print(i, i+d)
        break
else:
    print(-1)