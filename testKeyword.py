import keyword
import sys
from sys import argv, path  # 导入特定的成员

print(keyword.kwlist)

'''
这是注释
'''

"""
这也是注释
"""

# 这还是注释

# 多行语句

total = 1 + \
        2 + \
        3
print(total)

print("************************************")
str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

test1 = []
print(test1)

test2 = [1, ]
print(test2)

test21 = [1]
print(test21)

test3 = ()
print(test3)

test4 = (1,)
print(test4)
print(test4[0])
