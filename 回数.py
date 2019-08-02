# 回数.py


digits=[]
for i in range(10,1000):
    temp=str(i)             #数字转字符串
    digit=temp[::-1]        #字符颠倒次序
    if temp==digit:
        digits.append(int(temp))

print(digits)
