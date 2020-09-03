"""
当前进度：P6 04：38
目标：P22
"""
# 流程控制语句if
# why：生活中选择，回家有n条路，你走哪条路，取决于心情。
# what：if.
# how:
#   基本结构：
#   if 条件 :
#       结果
# 1.单独if
'''
condition = True
if condition:
    print(type(condition))
'''
# 2.if else
'''
age = int(input('请输入年龄：'))
if age > 18:
    print('成年了')
else:
    print('未成年')
'''
# if elif elif ...else 多选一
# 3.从上至下依次判断
'''
num = int(input('猜点数：'))
if num == 1:
    print('请吃饭')
elif num == 2:
    print('看电影')
elif num == 3:
    print('溜达')
elif num == 4:
    print('大宝剑')
else:
    print('拉跨')
'''
# 4.嵌套的if
'''
if 条件：
    if 条件：
        if 条件：
            。。。
'''
username = input('请输入用户名')
password = input('请输入密码')
your_code = input('请输入验证码')
code = 'queer'
if your_code == code:
    if username == 'user' and password == 'qwd':
        print('登陆成功')
    else:
        print('用户名或密码错误')
else:
    print('验证码错误')

'''
每天的计划：
默写。
1.上午讲课：
    跟着老师的思路走，说。
    自己也要做好截图
    不懂就要问
    不建议用笔纸记录
    课间：敲代码，讨论题，出去浪。
2.下午：
    不要看视频（理论性的内容多，而且是重点）
    整理今天的内容，笔记。
        参考老师的，有自己的见解，整理一份 md文件。
        将老师上午所有的代码敲2~3遍。（晚上7点之前一定要完成）
    写作业
        基础作业必须做完
        选做题：尝试做
        面试题：简单的必须做，难的尝试做，第二天必须会做。
    半个小时预习
    打字慢的同学：金山打字通，练习打字英文字半小时。160~180字符每分钟。
每周：思维导图（待续）。
每周一个大作业：打分的。
'''