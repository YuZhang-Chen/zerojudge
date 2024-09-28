while 1:
    try:
        n=int(input())
        if n==0:
            print(2)
        else:
            r=[2]
            for i in range(n):
                r.append(2**(i+2))
                if i>=9:
                    r.pop(0)
            print(sum(r))
    except:
        break