while 1:
    s=input().split()
    if s[0]=='END':
        break
    name=s[0]
    mb=float(s[1])
    mv=float(s[2])
    x=mb-mv
    if x>=-0.35 and x<=-0.251:
        color='O'
    elif x>=-0.25 and x<=-0.001:
        color='B'
    elif x>=0 and x<=0.249:
        color='A'
    elif x>=0.25 and x<=0.499:
        color='F'
    elif x>=0.5 and x<=0.999:
        color='G'
    elif x>=1 and x<=1.499:
        color='K'
    elif x>=1.5 and x<=2:
        color='M'
    
    print('%s %.2f %s'%(name,x,color))