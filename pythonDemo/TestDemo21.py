# 使用sorted()函数
def sortStr(lt):
    res = sorted(lst, key=len)
    return list(res)


lst = ["aa", "bbbb", "ccc", "d"]
result = sortStr(lst)
print("sorted()方法:", result)

#使用sort()方法
def sortStr(lt):
    lt.sort(key=len)
    return lt


lst = ["aa", "bbbb", "ccc", "d"]
result = sortStr(lst)
print("sort()方法:", result)
