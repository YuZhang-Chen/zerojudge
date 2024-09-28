while 1:
    s=input().split()
    if s[0]=='#':
        break
    distance=s[0]; phone_number=s[1]
    start_h=int(s[2]); start_m=int(s[3])
    end_h=int(s[4]); end_m=int(s[5])

    charging_stcp=['A','B','C','D','E']
    ratc=[
        [0.02,0.1,0.06,0.02,0.1,0.06,0.02],
        [0.05,0.25,0.15,0.05,0.25,0.15,0.05],
        [0.13,0.53,0.33,0.13,0.53,0.33,0.13],
        [0.17,0.87,0.47,0.17,0.87,0.47,0.17],
        [0.3,1.44,0.8,0.3,1.44,0.8,0.3]
        ]
    B=[480,1080,1320,1920,2520,2760,2880]

    time=[0]*7
    m1=start_h*60+start_m
    m2=end_h*60+end_m
    cost=0
    if m2<m1:
        m2+=24*60
    for i in range(7):
        if m1<=B[i]:
            if m2<=B[i]:
                time[i]=m2-m1
                idx=charging_stcp.index(distance)
                cost+=ratc[idx][i]*time[i]
                break
            else:
                time[i]=B[i]-m1
                idx=charging_stcp.index(distance)
                cost+=ratc[idx][i]*time[i]
                m1=B[i]

    print('%10s'%(phone_number), end='')
    print('%6d %5d'%(time[1]+time[4],time[2]+time[5]),end='')
    print('%6d'%(time[0]+time[3]+time[6]), end='')
    print('%3s %7.2f'%(distance,cost))