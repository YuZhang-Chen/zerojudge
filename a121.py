prm = [2, 3]
def f(n):
    if n < 2:
        return False
    for i in prm:
        if n%i == 0:
            return False
    return True

for i in range(4, 10001):
    if f(i):
        prm.append(i)

while True:
    try:
        ans = 0
        a, b = map(int, input().split())
        for i in range(a, b+1):
            if i < 10001 and i in prm:
                ans += 1
            elif f(i):
                ans += 1
        print(ans)
    except:
        break


"""
import sys
sys.setrecursionlimit(10001)

prime_bool = [True]*10001
prime_bool[0] = False
prime_bool[1] = False
prime = []
def f(n):
    prime.append(n)
    for i in range(n+n, len(prime_bool), n):
        prime_bool[i] = False
    try:
        idx = prime_bool.index(True, n+1)
    except:
        return
    f(idx)

def g(n):
    if n < 2:
        return False
    for i in prime:
        if n%i == 0:
            return False
    return True

f(2)

while True:
    try:
        a, b = map(int, input().split())
        ans = 0
        for i in range(a, b+1):
            if i < 10001 and prime_bool[i]:
                ans += 1
            elif g(i):
                ans += 1
        print(ans)
    except:
        break
"""