dic={'0 1 0 1':'A',
    '0 1 1 1':'B',
    '0 0 1 0':'C',
    '1 1 0 1':'D',
    '1 0 0 0':'E',
    '1 1 0 0':'F'}

import sys
for s in sys.stdin:
    n=int(s)
    ans=''
    for i in range(n):
        s=sys.stdin.readline().strip()
        ans+=dic[s]
    print(ans)