for x in range(int(input())):
    a=input()
    b=input()
    print('Case %d:'%(x+1), end=' ')
    if a==b:
        print('Yes')
    else:
        a=a.replace(' ','')
        b=b.replace(' ','')
        if a==b:
            print('Output Format Error')
        else:
            print('Wrong Answer')