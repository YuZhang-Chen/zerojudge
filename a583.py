data=[]
num=[]
n,m=map(int, input().split())
s=list(map(int, input().split()))
for i in range(m):
    tmp=[]
    a=s.pop(0)
    b=s.pop(0)
    tmp.append(a)
    tmp.append(b)
    data.append(tmp)

for i in range(len(data)):
    for j in range(i+1,len(data)):
        distance=((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2)**0.5
        num.append(distance)
ans=min(num)
print('%.4f'%(ans))