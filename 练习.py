# 练习一
# name =input("\033[33m\033[1m你的名字:")
# sex = input("你的性别：")
# jbo = input("你的职业：")
# number = input("你的电话号码:")
# print("-"*5, "infomation of {}","-"*5 )
# print('''name: {}
# sex: {}
# job: {}
# umber: {} ''' .format(name,sex,jbo,number))

# 练习二 判断输入的字符是否为数字
# char = input("随意输入:")
# if char.isdigit():
#     print("是数字")
# elif char.isalpha():
#     if char.isupper():
#         print("是纯大写字母")
#     elif char.islower():
#         print("是纯小写字母")
#     else:
#         print("混合字母")
# else:
#     print("是其他")

# 练习三 通过os模块判断操作系统上的文件是否存在
# import os
# file = input("输入路径:")
# if os.path.exists(file):
#     print("路径存在")
# else:
#     print("路径不存在")

# 练习四 使用getpass模块使用密码隐藏输入

# import getpass
# name = input("用户名:")
# password = getpass.getpass("密码:")
# if name == "devops" and password == "123":
#     print("登录成功")
# else:
#     print("密码或用户名错误")

# 练习五 通过年龄是否成年与性别来判断对一个人的称呼
# sex = input("性别:")
# age = int(input("年龄:"))
# if age > 18 :
#     if sex == "man":
#         print("先生你好")
#     else:
#         print("小姐姐有男朋友吗")
# else:
#     if sex == "man":
#         print("滚去学习")
#     else:
#         print("emmm....")

# 练习六 input输入一个年份,判断是否为闰年(能被4整除但不能被100整除的是闰年，或者能被400整除的也是闰年)

# year = int(input("输入年份"))
# if year % 4 == 0 and year % 100 != 0 :
#     print("%s 是闰年" % (year))
# else:
#     print("不是闰年")

# 练习七 打印1到100 和求和
# for i in range(2,100,2):
#     print(i,end=" ")

# i=0
# while i <= 100:
#     print(i,end=" ")
#     i += 2
# range 不包含102 到100就结束了
# sum = 0
# for i in range(0,102,2):
#     sum += i
# print(sum)

# num = 0
# sum = 0
# while num <= 100 :
#     sum += num
#     num += 2
# print(sum)



# 练习八  用for循环来实现 1-100之间能被 5整除,同时能被3整除的数的和

# sum = 0
# for i in range(0,101,1):
#     if i % 5 == 0 and i %  3 == 0  :
#         sum += i
#
# print(sum)

# 练习九 打印九九乘法表
# for i in range(1, 10, 1):
#     for y in range(1,i+1,1):
#         print("{} * {} =".format(y,i),y * i,end="  ")
#     print()

# 练习十 猜数字
# import random
# unm = random.randint(1,100)
# while True:
#     nnm = int(input("猜数字："))
#     if nnm > unm :
#         print("大了")
#         continue
#     elif nnm < unm :
#         print("小了")
#         continue
#     else:
#         print("真聪明哈哈哈哈")
#         break
#aaa
# 练习十一 一个袋子里有3个红球，3个绿球，6个黄球，一次从袋子里取6个球，列出所有可能组合
mmm = 0
for i in range(0,4,1):
    for y in range(0,4,1):
        for m in range(0,7,1):
            if i+y+m == 6 :
                print(i, y, m, end=" ")
                sum += 1
# print(sum)

# 练习十二 打印1-1000的质数（只能被1和自己整除的数)(未完成)
for i in range(1001):

        print("不是质数")


#这是一个注释

#  这是一个注释