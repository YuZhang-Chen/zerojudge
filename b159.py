while 1:
    try:
        l=[]
        w=int(input())
        n=int(input())
        for i in range(n):
            p=int(input())
            l.append(p)
        l=sorted(l, reverse=True)
        cnt=0
        while l!=[]:
            if len(l)==1:
                cnt+=1
                del l[0]
            elif l[0]+l[-1]<=w:
                cnt+=1
                del l[0]
                del l[-1]
            elif l[0]+l[-1]>w:
                cnt+=1
                del l[0]
        print(cnt)
    except:
        break