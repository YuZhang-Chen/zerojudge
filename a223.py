#檢查字串長度的因數這幾點就好
while True:
    s=input().strip()
    if s==".":
        break
    l=len(s) #字串長度
    if s==s[::-1]: #ex."AAAA"
        print(l)
        continue
    factor=[] #因數
    for i in range(2, l): #找因數
        if l%i==0:
            factor.append(i)

    for fac in factor:
        idx=s[0:fac]
        k=l//fac #倍數
        if idx*k==s: #ex."AB"*3 = "ABABAB"
            print(k)
            break
    else:
        print(1)
