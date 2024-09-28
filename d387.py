def f(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

while 1:
    try:
        n=input()
        if not f(int(n)):
            print(n, 'is not prime.')
        else:
            n1=n[::-1]
            if n==n1:
                print(n, 'is prime.')
            elif f(int(n)) and f(int(n1)):
                print(n, 'is emirp.')
            else:
                print(n, 'is prime.')
    except:
        break