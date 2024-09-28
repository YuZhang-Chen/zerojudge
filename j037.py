while 1:
    s=list(map(int, input().split()))
    if s[0]==0:
        break
    s.sort()
    a,b,c=s
    if a*a+b*b==c*c:
        print('right')
    else:
        print('wrong')