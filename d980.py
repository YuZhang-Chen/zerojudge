for x in range(int(input())):
    print('Case %d:'%(x+1), end=' ')
    s=list(map(int, input().split()))
    s.sort()
    a=s[0]
    b=s[1]
    c=s[2]
    if a<=0 or b<=0 or c<=0:
        print('Invalid')
    elif a+b<=c:
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')