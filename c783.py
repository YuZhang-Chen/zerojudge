def f(n):
    n=str(n)
    sum=0
    for i in n:
        sum+=int(i)
    return sum

for _ in range(int(input())):
    n=input().strip()
    if len(n)==1:
        print(int(n))
    else:
        number=int('9'*(len(n)-1))
        n=int(n)
        print(f(number)+f(n-number))