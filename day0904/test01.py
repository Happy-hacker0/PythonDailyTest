"""
目前进度：P14 00:03
今日目标：P30
"""
i1 = 100
i2 = 3
# ** 次幂
print(2 ** 3)
# // 整除
print(10 // 3)

print(3 != 4)

# and or but
# 1. 在没有括号的情况下，优先级：not > and > or,同一优先级从左至右以此计算
# 情况1：两边都是比较运算
print(2 > 1 and 3 < 4 and 2 < 1)

# 情况2：两边都是整数
'''
x or y ,x为真，值就是x，x为假，值就是y
'''
print(1 or 2)
print(3 or 2)
print(4 or 2)
print(-1 or 2)
print(0 or 2)

# str--->int: 只能是纯数字组成的字符串才能转成数字
s1 = '100'
print(int(s1))
# int--->str
i3 = 100
print(str(i3), type(str(i3)))
# int--->bool : 非零即True，0是False
i = 100
print(bool(100))
# bool--->int
print(int(True))  # 1
print(int(False))  # 0

# 面试题
print(1 and 2 or 3 and 4)  # 2

# 思考题
print(1 > 2 and 3 or 6)  # 6
