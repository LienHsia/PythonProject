def digits_reversed():
    num = input("请输入任意一个整数或小数：")
    digits_reversed = []
    if num[0] == '-':
        digits_reversed.append('-')
        num = num[1:]
    for i in range(len(num)-1,-1,-1):
        digits_reversed.append(num[i])
    print(float(''.join(digits_reversed)))

digits_reversed()
