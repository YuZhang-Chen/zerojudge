pos=['E','S','W','N']
suit=['C','D','S','H']
num=[str(i) for i in range(2,10)]+['T','J','Q','K','A']

while 1:
    d=input()
    if d=='#':
        break
    player=[[] for _ in range(4)]
    for _ in range(2):
        s=input()
        for i in range(0,len(s)-1,2):
            card=s[i]+s[i+1]
            player[pos.index(d)].append((card,suit.index(card[0]),num.index(card[1])))
            d=pos[(pos.index(d)+1)%4]

    for i in range(4):
        player[i]=sorted(player[i], key=lambda x:(x[1],x[2]))
        print('%s:'%(pos[(i+1)%4]), end=' ')
        for j in player[i]:
            print(*j[:1], end=' ')
        print()