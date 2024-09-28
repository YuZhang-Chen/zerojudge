from bisect import bisect_right

n=int(input())
data=[]
for _ in range(n):
    x, y=map(int, input().split())
    data.append((x, y))

data.sort()
tmp=[]
for _, i in data:
    if not tmp or tmp[-1]<=i:
        tmp.append(i)
    else:
        tmp[bisect_right(tmp, i)]=i

#print(tmp)
print(len(tmp))