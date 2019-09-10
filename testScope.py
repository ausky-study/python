# 测试作用域

total = 0


def sum(a, b):
    total = a + b
    print("函数total此时变成了局部变量", total)
    return total


sum(19, 20)
print("函数外是全局变量 : ", total)

listA = []


def sum(a, b):
    global listA
    print("函数total此时变成了局部变量", listA)
    listA = [a, b]
    return total


sum(19, 20)
print("函数外是全局变量 : ", listA)
