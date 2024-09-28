dic={
    'aa':'a',
    'ae':'a',
    'ai':'ai',
    'ay':'a',
    'ao':'w',
    'aou':'w',
    'aw':'w',
    'ea':'y',
    'ee':'ei',
    'ei':'ei',
    'ey':'y',
    'eo':'ou',
    'eou':'ou',
    'ew':'w',
    'oa':'w',
    'oe':'ou',
    'oi':'oi',
    'oy':'w',
    'oo':'ou',
    'oou':'ou',
    'ow':'w'
}

while 1:
    s=input().split('-')
    if s[0]=='END':
        break
    a=s[0]; b=s[1]
    if b[:2]=='ou':
        idx=a[-1:]+b[:2]
        b=b[2:]
    else:
        idx=a[-1:]+b[:1]
        b=b[1:]
    a=a[:-1]
    print(a+dic[idx]+b)