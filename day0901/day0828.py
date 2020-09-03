# day01 变量 常量 注释
print('hello 老铁！')

# 变量的小高级
# 变量好比是日常生活中的便利贴 给数据18贴上一个便利贴，起一个别名‘age1’
# 用来代指一些复杂过长的数据
age1 = 18
age2 = age1
age3 = age2
age2 = 12
print(age1, age2, age3)

# 常量
# why：生活中一直不变的：π，性别，身份证号。。。
# what：一直不变的量，python中没有真正的变量，为了迎合其他语言的口味，全部大写的变量称之为常量
# where: 设置一些不变的量
# how：将变量名全部大写，放在文件的最上面
NAME = '朱志鹏'
print(NAME)

# 注释
# why： 文言文中对一些晦涩难懂的成语或者经典的出处 解释说明。便于你理解。
# what: 注释
# how：单行注释：#
#      多行注释：'''注释''' 或者 """注释"""
# where: 难以理解的代码后面，加以注释。包括函数，类，文件说明等 都需要注释

# 基础数据类型初识
# why: 人类接触一些信息会做一些比较精准的划分。数字，汉字，英文。。。而机器不会进行划分。
# python的基础数据类型：
# int(整形)：用于运算
i = 100
i1 = 2
i2 = i * i1
print(i2)
# str: 凡是用引号引起来的数据就称之为字符串（'',"",'''''',""""""）
# 单双引号可以配合使用
s1 = 'day01'
s2 = 'python22期'
s3 = '''Python22期'''
print(s1, s2)
# content = 'I am taiBai, 18 year old'
content = "I'm taiBai, 18 year old"
print(content)
# 三引号：换行的字符串
msg = '''
aaa
aaa
aaa
'''
print(msg)
# 字符串可否加减乘除？ + *
# str + str : 字符串的拼接
s1 = 'alex'
s2 = 'sb'
print(s1 + s2)
# str * int
s1 = '坚强'
print(s1 * 10)

# bool：True False
print(2 > 1)
print(3 < 1)
print(True)
print('True')

# 判断变量指向的是什么数据类型 ：type()
s1 = '100'
s2 = 100
print(s1, type(s1))
print(s2, type(s2))

# 用户交互 input(出来的都是字符串类型)
# why：网页上，app输入账号与密码
# what：用户交互input
# how：
# user_name = input('请输入用户名：')
# Password = input('请输入密码：')
# print(user_name, type(user_name))
# print(Password, type(Password))

# 练习：让用户输入姓名， 年龄， 性别， 然后打印一句话‘我叫： ， 今年： ，性别：’
name = input('请输入姓名：')
age = input('请输入年龄：')
sex = input('请输入性别：')
print('我叫：' + name + ', 今年：' + age + ', 性别：' + sex)


