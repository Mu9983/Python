# # 三种格式化输出

# name = "张三"
# age = 12
# print("姓名：{}, 年龄：{}".format(name, age))
# print(f"{name}")
# print("姓名：%s，年龄：%d" % (name, age))

# # 字符串的按序打印及分割
# school_name = "HITwh"
# print("school_name[2:5]")
# print(f"{school_name[::-1]}")

# [num1 : num2] : 从num1到num2
# 下标为负时，表示从后往前数，最后一位为-1
# ::-1表示从后往前倒叙打印

# print(school_name[0: -0])
# 当num1与num2为[0: -0]时，无意义

# print(f"\"HIT\">\"HITwh\":{"HIT">"HITwh"}")
# 字符串也可使用大于小于号进行比较字符串长度大小

"""
if {表达式}:
    {执行命令}
elif {表达式}:
    {执行命令}
else:
    {执行命令}
"""
# #################
"""
while {表达式}:
    {执行命令}
"""
# #################
"""
for {临时变量} in [待处理序列]:
    {执行命令}

# name = "张三"
# for i in name:
#     print(i)
"""

# 练习
# name = "itheima is a brand of itcast"
# count = 0
# for i in name:
#     if i == 'a':
#         count += 1
# print(f"{name}中有{count}个a")

# 通过range语句获取简单的数字序列

# # for i in range(num1,num2,step)
# for i in range(10):
#     # 从0开始，包含0，不包含10
#     print(i)
#     # 每次打印自动换行
# for i in range(5,10):
#     # 包含5，不包含10
#     print(i)
# for i in range(2,10,3):
#     # 3为步长step，表示隔几个数字一打印
#     print(i)
# # 规范上不允许在for外部访问i，但实际上可以访问i
# print(i)# 此时使用i不会报错，只会报警告，易于产生bug, 建议使用后对i进行删除
# del i
# print(i)# 此时再使用i会报错

# money = 10000
#
# for i in range(1,21):
#     import random
#     score = random.randint(1,10)
#     if score < 5:
#         continue
#     elif money == 0:
#         break
#     else:
#         print(f"员工{i}领到了1000元工资")
#         money -= 1000
# print("工资发完了")

# match 等同于 switch

# str1 = "itheima"
#
# def mylen(data):
#     count = 0
#     for i in data:
#         count += 1
#     print("1")


# a = [[],[],[]]
# for i in range(3):
#     import random
#     for j in range(3):
#         a[i].append(random.randint(1,10))
#
# for i in range(3):
#     for j in range(3):
#         print(a[i][j])

# def mySQL(x, y):
#     """
#     :param x:
#     :param y:
#     :return:
#     """

# money = 5000000
# def login():
#     name = input("您好，欢迎来到ATM机，请输入您的姓名：")
#     return name
#
# def menu():
#     print("您好，欢迎来到ATM")
#     print("查询余额\t1\n存款\t2\n取款\t3\n退出\t4")
#     choice = input("请输入您想要办理的业务：")
#     return int(choice)
#
# def check(name1, money1):
#     print(f"{name1}，您好，您的余额为{money1}元")
#
# def checkin(name2, money2):
#     checkin_money = input("请输入存款金额:")
#     money2 += int(checkin_money)
#     print(f"{name2}，您好，存款{checkin_money}成功，当前余额：{money2}元")
#     return int(money2)
#
# def checkout(name3, money3):
#     checkout_money = input("请输入取款金额:")
#     if money3 < int(checkout_money):
#         print("余额不足，无法取款")
#     else:
#         money3 -= int(checkout_money)
#         print(f"{name3}，您好，取款{checkout_money}成功，当前余额：{money3}元")
#         return int(money3)
#
# def exit(name4):
#     print(f"{name4}，您已成功退出")
#
#
# name = login()
# while 1:
#     choice = menu()
#     match choice:
#         case 1:
#             check(name, money)
#         case 2:
#             money = checkin(name, money)
#         case 3:
#             money = checkout(name, money)
#         case 4:
#             exit(name)
#             break

# 列表操作
# 查询元素再列表内的下标
mylist = ["name", 'x', 3]
# 列表.index(元素)
index = mylist.index(3)

# 插入元素
# 列表.insert(下标,元素)
mylist.insert(1, "hello")

# 追加单个元素
# 列表.append(元素)
mylist. append(100)

# 追加批量元素
# 列表.extend(数据容器)
mylist2 = ["bye", 2, 3.14]
mylist.extend(mylist2)

# 删除元素
# del 列表[下标] 或 列表.pop(下标)
del mylist[3]
element = mylist.pop(3)
# 列表.remove(元素) 删除多个同名元素时，只会删除下标小的哪个，非贪婪删除
mylist.remove("hello")
# 清空列表
# 列表.clear()
mylist.clear()

# 统计某元素在列表中的出现次数
# 列表.count(元素)
mylist = ["hello", "hello", 1, 43, "hello"]
count = mylist.count("hello")

# 统计列表长度
# len(列表)
length = len(mylist)

# 元组 只读列表
# 定义：变量名 = (元素) 或 变量名 = tuple(元素)
mytuple = ("hello", "name", 1, 4, "你好")
mytuple2 = ()
# 当元组中只有一个元素时，需要在元素后加一个","，否则为字符串类型
mytuple3 = ("hello", )

# 元组内的列表是可以修改的
mytuple4 = (1, [2, 3, 4], 5)
mytuple4[1][1] = 6

# 字符串 只读不可修改
# str.index(元素)返回值为首元素的下标
string = "HITwh"
index2 = string.index('w')

# 替换 得到一个新的字符串，原来的字符串并没有变
# str.replace()
string2 = string.replace("wh", "HIT")

# 分割
# str.split(切割的元素)
string = "hello my friend"
string_split_list = string.split(" ")

# 去除字符串前后元素
# str.strip(去除元素) 去除的元素内部不论顺序，只要在字符串首尾，均去除
string = "   hello my friend    "
string4 = string.strip( )
string = "123 hello my friend 213"
string5 = string.strip("123 ")

# 空大括号为字典，定义空集合需要用到set()
set1 = set()
set2 = {1,2,3,4,5}

# 集合添加与删除
set2.add("1")
set2.remove(2)
set2.discard(4)

# 随机取出元素
element2 = set2.pop()

# 清空
set2.clear()

# 取差集
my_set1 = {1,2,3}
my_set2 = {1,2,5}
# 集合1的内容改变，集合2的内容不变
set_difference = my_set1.difference(my_set2)

# 取并集
my_set1 = {1,2,3}
# 原集合内容不变，得到一个新集合
set_union = my_set1.union(my_set2)

# 取交集
my_set1 = {1,2,3}
# 原集合内容不变，得到一个新集合
set_intersection = my_set1.intersection(my_set2)

# 由于集合去重，所以使用len()时，只统计不重复的元素个数

# 集合不支持下标操作，故while循环无效，只可使用for

# 字典
# 字典不允许key的重复，如果重复，后一个key的value会覆盖前一个的value
my_dict = {'1':1, '2':2, '3':3}
# 元素获取
element3 = my_dict['2']
# 字典的key和value可以是任何数据类型(key不可是dict)
my_dict2 = {"Tom":{"math":89, "Chinese":90},"Rose":{"math":90, "Chinese":92}}

# 修改与新增
# 字典[key] = value 若key存在，则为修改，若key不存在，则为新增

# 删除
# dict.pop(key)

# 清空
# dict.clear()

# 获取全部的key
# dict.keys()
keys = my_dict2.keys()    # keys的类型为<class 'dict_keys'>

# 字典转列表，元组，集合(且无序)时会将value值抛弃

# 容器排序

# 缺省传参
# 即C++中的默认参数

# 不定长传参
# 函数传参时，*args代表输入参数自动转为元组，**kwargs代表输入参数自动转为字典
# def user_info1(*args):
# user_info1(1,2,3,4)

# def user_info2(**kwargs):
# **kwargs传参时要使用“=”，不可使用“:”
# user_info2(name="Tom", age=11, gender="男")

def Caesar_encryption():
    """
    对后移三位的凯撒密码的实现
    """
    plaincode = input("请输入明文")
    b = ord('a')
    c = ord('A')
    for i in plaincode:
        if b <= ord(i) <= (b+26):
            print(chr((ord(i) - b + 3) % 26 + b), end='')
        elif c <= ord(i) <= (c+26):
            print(chr((ord(i) - c + 3) % 26 + c), end='')
        else:
            print(i,end='')

file = open("D:/DevelopingSoftware/Pycharm/PythonProject/LearnPython.py", 'r', encoding='UTF-8')
# 读取文件字符file.read(字符数) 输出结果为str
# 按行读取file.readlines() 输出结果为一个列表，每一行作为一个元素，且会读出\n
# 每次读取一行file.readline() 输出结果为一个字符串，不会读出\n

# 关闭文件
file.close()    #file.close()内置了file.flush()
# 可以使用with open(path, way, encoding) as <file>: 方法来进行读取，读取后自动关闭文件
with open("D:\\DevelopingSoftware\\Pycharm\\PythonProject\\test.txt", 'w', encoding='UTF-8') as file:
   file.write("print(1)")

with open("D:\\DevelopingSoftware\\Pycharm\\PythonProject\\test.txt", 'w', encoding='UTF-8') as file:
    file.write("The same to you")
    file.flush()

def Split_English_and_Chinese(string):
    """
    分割中文与英文
    :param string:待分割字符串
    """
    English_string = []
    Chinese_string = []
    switch = -1
    for i in string:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or i == ' ':
            if switch == 0:
                English_string.append(' ')
            English_string.append(i)
            switch = 1
        else:
            Chinese_string.append(i)
            switch = 0
    print("".join(English_string).strip(' '))
    print("".join(Chinese_string))
# Split_English_and_Chinese("我I很am厉害very good")


















