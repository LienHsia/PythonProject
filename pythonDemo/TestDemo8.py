def func(x):
    return x**2

map(func, [2,3,4,5])
print(map(func, [2,3,4,5]))
print(type(map(func, [2,3,4,5])))

res = map(func, [2,3,4,5])

for i in res:
    print(i)

list(map(func, [2,3,4,5]))

# 结果
"""
<map object at 0x0000022C5F15CB00>
<class 'map'>
4
9
16
25
[4, 9, 16, 25]
"""
