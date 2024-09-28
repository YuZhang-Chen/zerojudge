text="A=10 台北市     J=18 新竹縣     S=26 高雄縣 B=11 台中市     K=19 苗栗縣     T=27 屏東縣 C=12 基隆市     L=20 台中縣     U=28 花蓮縣 D=13 台南市     M=21 南投縣     V=29 台東縣 E=14 高雄市     N=22 彰化縣     W=32 金門縣 F=15 台北縣     O=35 新竹市     X=30 澎湖縣 G=16 宜蘭縣     P=23 雲林縣     Y=31 陽明山 H=17 桃園縣     Q=24 嘉義縣     Z=33 連江縣 I=34 嘉義市     R=25 台南縣"
text=text.replace("=", " ").split()
data=[]
alpha=[]
num=[]
for i in range(0, len(text), 3):
    alpha.append(text[i])
    num.append(text[i+1])

s=input()
sum=0
first_num=num[alpha.index(s[0])]
sum+=int(first_num[-1])*9+int(first_num[0])

for i in range(1, len(s)-1):
    sum+=int(s[i])*(9-i)
sum+=int(s[-1])
print("real" if sum%10==0 else "fake")