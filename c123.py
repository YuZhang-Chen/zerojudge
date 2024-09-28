while 1:
    n=int(input())
    if n==0:
        break
    while 1:
        s=list(map(int, input().split()))
        if s[0]==0:
            break
        train=[i for i in range(1,n+1)]
        station=[]
        output=[]
        idx=0
        while 1:
            if station==[]:
                station.append(train.pop(0))
            if s[idx]==station[-1]:
                output.append(station.pop())
                idx+=1
            else:
                station.append(train.pop(0))
            if train==[]:
                break
        
        while station:
            output.append(station.pop())
            
        if output==s:
            print('Yes')
        else:
            print('No')
    print()