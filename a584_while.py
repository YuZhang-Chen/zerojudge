dic={}
for _ in range(int(input())):
    s=input().split()
    node=s.pop(0)
    if node not in dic:
        dic[node]=s
    else:
        dic[node]+=s
    for i in s:
        if i not in dic:
            dic[i]=[node]
        else:
            dic[i]+=[node]

a,b=input().split()
distance={}
visited=[]
q=[(a,0)]
while len(q)>0:
    aa=q.pop(0)
    node=aa[0]
    d=aa[1]
    for i in dic[node]:
        if i not in visited:
            visited.append(i)
            q.append((i, d+1))
        if i not in distance:
            distance[i]=d+1
print(distance[b])