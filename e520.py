t=int(input())
for _ in range(t):
    ans=[]
    pq=[]
    n,k=map(int, input().split())
    medicine=[]
    time=[]
    for _ in range(n):
        m,f=input().split()
        f=int(f)
        medicine.append(m)
        time.append(f)
        pq.append([f,m,medicine.index(m)])

    while len(ans)!=k:
        pq=sorted(pq, key=lambda x:(x[0],x[2]))
        now=pq.pop(0)
        a,b,c=now[0],now[1],now[2]
        a+=time[medicine.index(b)]
        ans.append(now)
        pq.append([a,b,c])

    for i in ans:
        print(*i[:-1])