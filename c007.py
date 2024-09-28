cnt=1
while 1:
    try:
        s=input().replace('"','#')
        for i in s:
            if i=='#':
                if cnt%2==1:
                    print("``", end='')
                else:
                    print("''", end='')
                cnt+=1
            else:
                print(i, end='')
        print()
    except:
        break