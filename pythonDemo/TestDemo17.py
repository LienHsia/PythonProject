n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)
# 演进
try:
num = int(input("Enter a number: "))
except ValueError as err:
print(err)

dictio = dict()
for item in range(num+1):
if item == 0:
continue
else:
dictio[item] = item * item
print(dictio)n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)
# 演进
try:
num = int(input("Enter a number: "))
except ValueError as err:
print(err)

dictio = dict()
for item in range(num+1):
if item == 0:
continue
else:
dictio[item] = item * item
print(dictio)