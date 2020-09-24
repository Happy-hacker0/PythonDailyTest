# count = 0
# gift = 66
# while count < 3:
#     num = int(input("请输入数字："))
#     if gift == num:
#         print("bingo")
#         break
#     elif gift < num:
#         print("smaller")
#     else:
#         print("bigger");
#     count += 1
# else:
#     print("shabby")

# index = 1
# while index < 11:
#     print(index)
#     index += 1

# addition = 0
# i = 0
# while i < 101:
#     addition += i
#     i += 1
# print(addition)

# i = 1
# while i < 101:
#     if i % 2 == 0:
#         print(i, " ")
#     i += 1

# i = 1
# while i < 101:
#     if i % 2 != 0:
#         print(i, " ")
#     i += 1
#
# i = 1
# addition = 0
# while i < 101:
#     if i % 2 == 0:
#         addition -= i
#     else:
#         addition += i
#     i += 1
# print(addition)
count = 1
while count <= 3:
    username = input("请输入用户名：");
    password = input("请输入密码：");
    if username == 'zzp' and password == '123':
        print("登陆成功！")
        break
    else:
        print('''还剩 %d 次机会''' % (3 - count))
    count += 1
