dic = {}
def f(n):
    num_lst = []
    num = n
    while num != 1:
        num_lst.append(num)
        if num%2 == 1:
            num = 3*num+1
        else:
            num = num//2
    return len(num_lst)+1

while True:
    try:
        a, b = map(int, input().split())
        ans = [a, b]
        if a > b:
            a, b = b, a
        max_cyc_len = []
        for i in range(a, b+1):
            if i in dic:
                max_cyc_len.append(dic[i])
            else:
                cyc_len = f(i)
                dic[i] = cyc_len
                max_cyc_len.append(cyc_len)
        print(*ans, max(max_cyc_len))
    except:
        break