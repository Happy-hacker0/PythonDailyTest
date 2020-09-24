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


