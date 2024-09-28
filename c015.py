def f(n):
    n=str(n)
    num.append(n)
    n1=n[::-1]
    if n1==n:
        return
    f(int(n1)+int(n))

for _ in range(int(input())):
    num=[]
    n=int(input())
    if str(n)==str(n)[::-1]:
        num.append(str(n))
        n+=int(str(n)[::-1])
    f(n)
    print(len(num)-1, num[-1])