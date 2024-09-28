dic={
    'HELLO':'ENGLISH',
    'HOLA':'SPANISH',
    'HALLO':'GERMAN',
    'BONJOUR':'FRENCH',
    'CIAO':'ITALIAN',
    'ZDRAVSTVUJTE':'RUSSIAN'
}

cnt=0
while 1:
    s=input()
    if s=='#':
        break
    cnt+=1
    if s not in dic:
        print('Case %d: UNKNOWN'%(cnt))
    else:
        print('Case %d: %s'%(cnt,dic[s]))