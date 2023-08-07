def check(element):
    return all(ord(i)%2 == 0 for i in element)  ＃所有返回true如果所有的数字，i是即使在元件
 
lst = [str(i) for i in range(1000,3001)]        ＃创建所有给定数字的列表，其字符串数据类型为
lst = list(filter(check,lst))                   ＃如果检查条件失败，则过滤器从列表中删除元素
print(",".join(lst))
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   ＃使用lambda来在过滤器功能内部定义函数
print(",".join(lst))