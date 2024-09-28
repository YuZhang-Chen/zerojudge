num=[]
for i in range(121):
    num.append(4**i)

while 1:
    try:
        n=int(input())
        print(sum(num[:n]))
    except:
        break