while 1:
    try:
        B,P,M=map(int, input().split())
        print(pow(B,P,M))
    except:
        break