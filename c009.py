while 1:
    n=input()
    if n=='-1':
        break
    if n.isdigit():
        n=int(n)
        ans=hex(n)[2:].upper()
        print('0x'+ans)
    else:
        n=n[2:]
        print(int(n, 16))