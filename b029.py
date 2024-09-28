n,k=map(int, input().split())
for _ in range(n):
    x=list(map(int, input().split()))
    y=list(map(int, input().split()))
    x.sort()
    y.sort()
    sum=0
    #ans=[]
    #for i in range(k):
    #    if i>0:
    #        ans.append('+')
    #    ans.append(str(x[i])+'*'+str(y[i]))
    for i in range(k):
        sum+=x[i]*y[i]
    print(sum)