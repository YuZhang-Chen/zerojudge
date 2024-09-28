dic={
    'B':1,'P':1,'F':1,'V':1,
    'C':2,'S':2,'K':2,'G':2,'J':2,'Q':2,'X':2,'Z':2,
    'D':3,'T':3,
    'L':4,
    'M':5,'N':5,
    'R':6
}

print('NAME                     SOUNDEX CODE')
while 1:
    try:
        soundex=''
        s=input().strip()
        soundex+=s[0]
        for i in range(1,len(s)):
            if dic.get(s[i])==dic.get(s[i-1]):
                continue
            if s[i] in dic:
                soundex+=str(dic[s[i]])
        soundex=soundex.ljust(4,'0')
        soundex=soundex[:4]
        print('         %-20s'%(s),end='')
        print('%9s'%(soundex))
    except:
        break
print('                   END OF OUTPUT')