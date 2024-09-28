for _ in range(int(input())):
    D,I=map(int, input().split())
    idx=1
    remainder=I
    for i in range(D-1):
        if remainder%2==1:
            idx=2*idx
            remainder=(remainder+1)//2
        else:
            idx=2*idx+1
            remainder//=2
    print(idx)