N=int(input())
xx=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int, input().split())))

dxy=[(0,-1),(-1,0),(0,1),(1,0)]
step=1 #要走幾步
step_cnt=0
cnt=1 #總共
f=N//2
r=f
c=f

print(arr[f][f], end='')
while cnt<N*N:
    for i in range(step):
        r+=dxy[xx%4][0]
        c+=dxy[xx%4][1]
        if r<0 or c<0 or r>=N or c>=N:
            break
        print(arr[r][c], end='')
        cnt+=1
    xx+=1
    step_cnt+=1
    if step_cnt==2:
        step_cnt=0
        step+=1