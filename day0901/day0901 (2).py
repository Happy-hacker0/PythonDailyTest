"""
当前进度：P11 01：33
目标：P22
"""
# while循环 基本结构
'''
while 条件：
    循环体
'''
'''
while True:
    print('达拉蹦吧')
    print('我们不一样')
    print('兄弟')
'''

# 循环如何终止
'''
condition = True
num = 0
while condition:
    num += 1
    if num < 10:
        print(num, ",")
    else:
        break
'''


# 输出一到一百所有数字
num = 1
while num < 101:
    print(num)
    num += 1

# 输出一到一百的和
Sum = 0
num = 1
while num < 101:
    Sum += num
    num += 1
print(Sum)

# continue: 推出本次循环，继续下一次循环
num = 0
while num < 101:
    num += 1
    if num % 2 == 0:
        continue
    else:
        print(num)

# while else：while循环如果被break打断，则不执行else语句
count = 1
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1
else:
    print(666)

