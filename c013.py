for _ in range(int(input())):
    if _==0:
        input()
    a=int(input())
    f=int(input())
    for i in range(f):
        for j in range(1,a+1):
            print(str(j)*j, end='')
            print()
        for j in range(a-1, 0,-1):
            print(str(j)*j, end='')
            print()
        print()