# 格式化输出
# msg = '''
# ----info of zzp----
# Name: zzp
# Age : 21
# Job = Student
# --------end--------
# '''

# 制作一个公共的模板
# 让一个字符串的某些位置变成动态可传入的
# 格式化输出
name = input("Name:")
age = input("Age:")
job = input("Job:")

# %: 占位符 s-->str d i r
msg = '''
-----info of %s-----
Name: %s
Age : %d
Job = %s
---------end--------
''' % (name, name, int(age), job)
print(msg)

# 坑：在格式化输出中，只想表示一个百分号，而不是作为占位符使用 eg：1%
# 需要这么写：%%
msg = '我叫%s,今年%s,学习进度1%%' % ('zzp', '18')
print(msg)
