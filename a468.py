month=["", "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"]

for _ in range(int(input())):
    d1=input().replace(",", "").split()
    d2=input().replace(",", "").split()
    m1, d1, y1=d1
    m2, d2, y2=d2
    d1=int(d1)
    y1=int(y1)
    d2=int(d2)
    y2=int(y2)
    
    idx_m1=month.index(m1)
    idx_m2=month.index(m2)
    if idx_m1==1 or idx_m1==2:
        y1-=1
    if idx_m2==1 or idx_m2==2:
       y2-=1
    if idx_m2==2 and d2==29:
        y2+=1

    cnt1=y1//4-y1//100+y1//400
    cnt2=y2//4-y2//100+y2//400

    print("Case %d: %d"%(_+1, cnt2-cnt1))