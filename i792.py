input()
board=list(map(int, input().split()))
board=sorted(board)
G=list(map(int, input().split()))
gift=0
ans=0

while len(board)>0:
    aa=board.pop()
    ans+=aa*gift
    g=G.pop(0)
    gift+=g
print(ans)