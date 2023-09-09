#1.长方形完整格式
#完整格式输出九九乘法表
for i in range(1,10):
 for j in range(1,10):
 print("%d*%d=%2d" % (i,j,i*j),end=" ")
 print("")
#2.左上三角形

#左上三角格式输出九九乘法表
for i in range(1,10):
 for j in range(i,10):
 print("%d*%d=%2d" % (i,j,i*j),end=" ")
 print("")

#3.右上三角形

#右上三角格式输出九九乘法表
for i in range(1,10):
 for k in range(1,i):
 print (end="       ")
 for j in range(i,10):
 print("%d*%d=%2d" % (i,j,i*j),end=" ")
 print("")

#4.左下三角形

#左下三角格式输出九九乘法表
for i in range(1,10):
 for j in range(1,i+1):
 print("%d*%d=%2d" % (i,j,i*j),end=" ")
 print (" ")

# 5.右下三角形

#右下三角格式输出九九乘法表
for i in range(1,10):
 for k in range(1,10-i):
 print(end="       ")
 for j in range(1,i+1):
        product=i*j
 print("%d*%d=%2d" % (i,j,product),end=" ")
 print (" ")