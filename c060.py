while True:
    try:
        s = list(map(int, input().split()))
        num = []
        ans = ""
        for i in range(len(s)-1):
            if s[i] != 0:
                if s[i] == 1 or s[i] == -1:
                    if s[i] > 0:
                        num.append("x^" + str(len(s)-i-1) if str(len(s)-i-1) != "1" else "x")
                    else:
                        num.append("-x^" + str(len(s)-i-1) if str(len(s)-i-1) != "1" else "-x")
                else:
                    num.append(str(s[i]) + "x^" + str(len(s)-i-1) if str(len(s)-i-1) != "1" else str(s[i]) + "x")

        for i in range(len(num)):
            if i == 0:
                ans += num[i]
            else:
                if num[i][0] == "-":
                    ans += " - " + num[i][1:]
                else:
                    ans += " + " + num[i]

        if s[-1] != 0:
            if not ans:
                ans += str(s[-1])
            else:
                if s[-1] > 0:
                    ans += " + " + str(s[-1])
                else:
                    ans += " - " + str(-s[-1])
        print(ans if ans else "0")
    except:
        break