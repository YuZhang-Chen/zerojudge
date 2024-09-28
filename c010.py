import bisect

num=[]
while 1:
    try:
        n=int(input())
        idx=bisect.bisect_left(num, n)
        num.insert(idx, n)
        l=len(num)
        if l%2==0:
            print((num[l//2]+num[l//2-1])//2)
        else:
            print(num[l//2])
    except:
        break