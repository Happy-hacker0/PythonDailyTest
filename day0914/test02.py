s = 'python全栈22期'
# 从左至右都是有顺序的，下标，索引。
# 对字符串进行索引，切片出来的数据都是字符串类型
# 按照索引取值
# s1 = s1[0]
# print(s2, type(s2))
# s2 = s1[2]
# print(s3)
# s3 = s1[-1]
# print(s4)
# s4 = s1[-2]
# print(s5)


# 按照切片取值。
# 左闭右开
# 如果从0开始 0可以省略不写
s5 = s[0:6]
print(s5)
# 取到结尾冒号后面什么也不写
s6 = s[6:]
print(s6)

# 切片步长
s7 = s[:5:2]
print(s7)

# 倒叙：一定要加一个反向的步长
s8 = s[-1:-6:-1]
print(s8)

"""
按照索引：s[index]
按照切片：s[start_index: end_index+1]
按照切片步长：s[start_index: end_index+1: 步长]
按照反向切片步长：s[start_index: end_index后延一位: 反向步长]
"""
print(s[::-1])

# 练习题
s = '123a4b5c'
s1 = s[:3]  # 123
s2 = s[3:6]  # a4b
s3 = s[::2]  # 1345
s4 = s[1:-2:2]  # 2ab
s5 = s[-1]  # c
s6 = s[-3::-2]  # ba2
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
