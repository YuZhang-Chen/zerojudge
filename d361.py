while 1:
    m,n=map(int, input().split())
    if m==0 and n==0:
        break
    print(pow(m,n,10))