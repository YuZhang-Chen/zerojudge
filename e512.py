while 1:
    try:
        a1,a2,b1,b2,c1,c2,d1,d2=map(float, input().split())
        if a1==d1 and a2==d2:
            b1+=c1-d1
            b2+=c2-d2
            print('%.3f %.3f'%(b1,b2))
        if a1==c1 and a2==c2:
            b1+=d1-c1
            b2+=d2-c2
            print('%.3f %.3f'%(b1,b2))
        if b1==d1 and b2==d2:
            a1+=c1-d1
            a2+=c2-d2
            print('%.3f %.3f'%(a1,a2))
        if b1==c1 and b2==c2:
            a1+=d1-c1
            a2+=d2-c2
            print('%.3f %.3f'%(a1,a2))
    except:
        break