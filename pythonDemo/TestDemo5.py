import random
import string

def passwordf():
    
    list_ = list(string.ascii_letters)+list(string.digits) + list("!@#$%^&*,./;\=+-()") #大小字母+数字+特殊符号
    n = int(input()) #n位密码
    password = []
    password = random.sample(list_, n)
    password_middle = [str(i) for i in password]
    password_end = ''.join(password_middle)    
    print(password_end)
    
passwordf()
