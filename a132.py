while 1:
    n=int(input())
    if n==0:
        break
    b=bin(n)[2:]
    print('The parity of %s is %d (mod 2).'%(b,b.count('1')))