w,h=map(int, input().split())
n=int(input())
arr=[]
alpha=[]
for i in range(w):
    arr.append([])
    s=input().split()
    for j in range(len(s)):
        if s[j].isalpha():
            alpha.append(s[j])
        arr[i].append(s[j])

alpha.sort()
f=True
ans=[]
for k in range(n):
    if len(alpha)==0:
        f=False
        break
    idx=alpha.pop(0)
    for i in range(w):
        if idx in arr[i]:
            ans.append((i, arr[i].index(idx)))

if f:
    for i in ans:
        print(*i)
else:
    print('Mission fail.')