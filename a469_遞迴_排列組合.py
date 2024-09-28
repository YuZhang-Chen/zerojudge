def f(idx, key=[]):
    if idx==len(k):
        print(''.join(key))
    else:
        for i in range(0,len(key)+1):
            key.insert(i, k[idx])
            f(idx+1, key)
            key.pop(i)

while 1:
    try:
        k=list(input())
        f(0,[])
        print()
    except:
        break