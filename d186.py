import math
while 1:
    a,b=map(int, input().split())
    if a==b==0:
        break
    print(math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1)