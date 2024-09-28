import math

for _ in range(int(input())):
    n,w=map(int, input().split())
    s=list(map(int, input().split()))
    for i in range(w):
        x=input().split()
        k=int(x[0])
        if k==3:
            e=int(x[1])
            print(s[e])
        else:
            x,y=int(x[1]),int(x[2])
            if k==1:
                mx=[s[j] for j in range(x,y+1)]
                print(max(mx))
            else:
                sum1=sum([s[j] for j in range(x,y+1)])
                ave=sum1/(y+1-x)
                if ave<0:
                    ave=math.ceil(ave)
                else:
                    ave=math.floor(ave)
                print(ave)