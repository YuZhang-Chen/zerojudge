cnt=0
while 1:
    Z,I,M,L=map(int, input().split())
    if Z==I==M==L:
        break
    cnt+=1
    cyc=[]
    while 1:
        cyc.append(L)
        new_num=(Z*L+I)%M
        if new_num in cyc:
            idx=new_num
            break
        L=new_num
    print('Case %d: %d'%(cnt, len(cyc[cyc.index(idx):])))