# int主要是用来计算的
"""
二进制和十进制互相转换
"""

# int
# bit_length: 有效的二进制长度
i = 4
print(i.bit_length())  # 3
i = 5
print(i.bit_length())  # 3
i = 10
print(i.bit_length())  # 4

# bool int str
# bool <---> int ***
"""
True 1  False 0
非零即True 0是False
"""

# str <---> int ***
"""
s1 = 10  int(s1):必须是数字组成
i = 100  str(i)
"""

# str <---> bool ***
# 非空即True
s = "adana"
print(bool(s))

s = ''  # 空字符串
print(bool(s))

# bool ---> str 无意义
print(str(False))

# 字符串的常用方法
s = 'taiBai'
# lower upper (遇到中文自动忽略)
# 不会对源字符串进行任何操作 都会产生一个新的字符串
s1 = s.upper()
print(s1)
print(s1, type(s1))

# 应用：
username = input("请输入用户名：")
password = input("请输入密码：")
code = "QweR"
your_code = input("请输入验证码：不区分大小写")
if your_code.upper() == code.upper():
    if username == "zzp" and password == "123":
        print("登陆成功")
    else:
        print("用户名或密码错误")
else:
    print('验证码错误')
