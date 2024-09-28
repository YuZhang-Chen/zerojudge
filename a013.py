def number(num):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ans = ""
    ans += M[num//1000]
    ans += C[num//100%10]
    ans += X[num//10%10]
    ans += I[num%10]
    
    return ans

def roma_num(roma):
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    pre = None
    for i in range(len(roma)):
        if (roma[i] == "X" or roma[i] == "V") and pre == "I":
            sum -= 2
        if (roma[i] == "C" or roma[i] == "L") and pre == "X":
            sum -= 20
        if (roma[i] == "D" or roma[i] == "M") and pre == "C":
            sum -= 200
        sum += dic[roma[i]]
        pre = roma[i]

    return sum

while True:
    s = input().split()
    if s[0] == "#":
        break
    a, b = s
    n = abs(roma_num(a)-roma_num(b))
    output = number(n)
    print(output if n!=0 else "ZERO")