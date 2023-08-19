import time

def add_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()

        print("time",end-start)

    return wrapper

@add_time
def my_count():
    s = 0
    for i in range(1000001):
        s += i
    print(s)

# 执行函数
my_count()