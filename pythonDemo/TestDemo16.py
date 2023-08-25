for i in '',[],(),{},{:}
#可以for循环的对象是可迭代对象。
a = (x for i in range(100))
#列表生成式，把中括号改为小括号就可以变为一个列表生成器，是可迭代对象。
from collections import Iterable #如果想验证是否是可迭代对象，可以使用isinstance()判断是否是可迭代对象。
isinstance('abc',Ierable) #判断语法
a = [1,2,3,4,5]
b = iter(a)  #使用iter()方法可以将可迭代对象转换为可迭代对象。