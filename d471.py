while 1:
    try:
        n=int(input())
        for i in range(0,2**n):
            print(bin(i)[2:].zfill(n))
    except:
        break