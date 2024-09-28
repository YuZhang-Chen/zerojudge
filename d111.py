while 1:
    n=int(input())
    if n==0:
        break
    if n**0.5==int(n**0.5):
        print('yes')
    else:
        print('no')