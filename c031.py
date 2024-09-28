while 1:
    try:
        n=int(input())
        slash=1
        term=1
        while term<n:
            term+=slash+1
            slash+=1
            part1=term-n+1
            part2=slash-part1+1
            
        if slash%2:
            print('TERM %d IS %d/%d'%(n, part1, part2))
        else:
            print('TERM %d IS %d/%d'%(n, part2, part1))
    except:
        break