# 方法一
lt1 = [1, 3, 5, 7, 9]
lt2 = [2, 4, 6, 8, 10]
res = [[lt1[i],lt2[i]] for i in range(5)]
print(res)

# 方法二
def unity(x, y):
    return [x, y]

lt1 = [1, 3, 5, 7, 9]
lt2 = [2, 4, 6, 8, 10]
res = map(unity, lt1, lt2)
print(list(res))

# 方法三
lt1 = [1, 3, 5, 7, 9]
lt2 = [2, 4, 6, 8, 10]
res = map(lambda x, y: [x, y], lt1, lt2)
print(list(res))
