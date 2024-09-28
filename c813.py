from sys import stdin
def f(n):
    n=str(n)
    return sum(list(map(int, list(n))))

for s in stdin:
    n=int(s)
    if n==0:
        break
    while n>9:
        n=f(n)
    print(n)