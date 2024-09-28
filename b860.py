kakuna=0
cnt=0
candy,w=map(int, input().split())
while w>0:
    mn=candy//12
    if w<mn:
        mn=w
    if mn:
        candy-=11*mn
        w-=mn
        kakuna+=mn
        cnt+=mn

    candy+=kakuna
    kakuna=0
    if candy<12:
        w-=12-candy
        candy=12

print(cnt)