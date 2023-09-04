lst = []

for i in range(1000,3001):
flag = 1
for j in str(i): ＃每个整数编号i被转换成字符串

if ord(j)%2 != 0: ＃ORD返回ASCII值并且j是i
flag = 0
if flag == 1:
lst.append(str(i)) ＃i作为字符串存储在列表中

print(",".join(lst))