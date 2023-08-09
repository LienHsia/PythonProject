def find_2(x):
    tmp=x
    f2=0 #记录因子2的个数
    f5=0 #记录因子5的个数
    while x%2==0:
        f2+=1
        x=x/2
    while tmp%5==0:
        f5+=1
        tmp/=5
    return f2,f5
#进行计算
L=[2,8,3,50]
a2=0 #记录列表中因子2的个数
a5=0 #记录列表中因子5的个数
for i in L:
    t2,t5=find_2(i)
    a2+=t2
    a5+=t5
print(min(a2,a5)) #2