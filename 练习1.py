# string1="hello"
# string2='hello'
# string3="""hello
# python"""
# string4='''hello
# world'''
# print(type(str(18)))
# print(isinstance(18,int))

# name="庞俊杰"
# print("你真聪明,",name)
# print("你真聪明," + name)
# print("你真聪明,%s" % (name) )
# print("你真聪明,{}".format(name))

# enumerate() 可以使用两个变量,调出下标
# name="devops"
# print(name[2:5])


# abc="hello,nice to meet you"
# print(len(abc))
# print(abc.__len__())
# print(abc.capitalize())
# print(abc.title())
# print(abc.upper())
# print(abc.lower())
# print("HAHAhehe".swapcase())
# print(len(abc.center(50,"*")))
# print(abc.ljust(50,"*"))
# print(abc.rjust(50,"*"))


# print("  haha\n".strip()) # 删除字符串左边和右边的空格或换行
# print("  haha\n".lstrip()) # 删除字符串左边的空格或换行
# print("  haha\n".rstrip())

# abc="hello,nice to meet you"
# print(abc.replace("e","E") )
# print("root:x:0:0".split("root"))
# print("root:x\n:0:0".splitlines())
# print("***".join(["df","-h"]))

# list=["刘招勋","王杰","小康康","旺仔","俊俊"]
# print(list[0::2])
# for j, i in enumerate(list):
#     print()
#     print(j+1,i+"取我的方天画戟，我要给秀儿削个苹果")

# print(list.reverse())
# print(list)


list=["刘招勋","王杰","小康康","旺仔","俊俊"]

# list.append("庞俊杰")
# print(list)
# print(id(list))
# list.insert(2,"弟弟")
# print(list)
# print(id(list))
# list.remove("弟弟")
# print(list)
# list[2]="康慧峰"
# print(list)

# math = ["张三", "田七", "李四", "马六"]
# english = ["李四", "王五", "田七", "陈八"]
# art = ["陈八", "张三", "田七", "赵九"]
# music = ["李四", "田七", "马六", "赵九"]
# # add.extend(app)
# # print(add)
#
# st1 =math + englist

# name_list = ["zhangsan", "lisi", "wangwu", "maliu"]
# salary = [18000, 16000, 20000, 15000]
#
# for j,i in enumerate(name_list):
#     print("%s的月薪是%s元" % (i,salary[j]))


# HAHA= (["zhangsan", 18000], ["lisi", 16000], ["wangwu", 20000], ["maliu", 15000])
# print(HAHA[0][1])
# HAHA[0][1] = 25000
# HAHA[0][0] = "tianqi"
# print(HAHA[0][1])
# print(HAHA)
#
# LOL = {
#     "上单": "魔法少女额加特",
#     "打野": "混分巨兽",
#     "中单": "托儿所"
# }
# LOL["adc"] = "金克斯"
# LOL["adc"] = "皮克斯"
# LOL.pop("上单")
#
# LOL["上单"] = "贾科斯"
# LOL["辅助"] = "仙灵女巫"
# LOL["adc"] = "金克斯"
# print(LOL)
# LOL.clear()
# print(LOL)



# city={
#     "北京": {
#         "东城":"景点",
#         "朝阳":"娱乐",
#         "海淀":"大学",
#     },
#     "深圳":{
#         "罗湖":"老城区",
#         "南山":"IT男聚集",
#         "福田":"华强北",
#     },
#     "上海":{
#         "黄埔":"xxxx",
#         "徐汇":"xxxx",
#         "静安":"xxxx",
#     },
# }
# print(city["北京"]["东城"])
# city["北京"]["东城"] = "故宫在这"
# print(city["北京"]["东城"])
# city["北京"]["昌平"] = "牛逼"
# print(city["北京"]["昌平"])
# city["北京"]["海淀"] = ["清华","北大","北邮"]
# print(city["北京"]["海淀"])
# city["北京"]["海淀"].append("北影")
# print(city["北京"]["海淀"])
# sum = 0
# for  i in city["北京"]:
#     print(sum+1,i[0:2])
#     sum += 1
# nnm = 0
# for j in city["北京"]["海淀"]:
#     print(nnm+1,j)
#     nnm += 1



# math = ["张三", "田七", "李四", "马六"]
# english = ["李四", "王五", "田七", "陈八"]
# art = ["陈八", "张三", "田七", "赵九"]
# music = ["李四", "田七", "马六", "赵九"]
#
# list = math + english + art + music
#
# det = {}
# for i in list:
#     if list.count(i) > 0:
#         det[i] = list.count(i)
#
# for j in det.items():
#     if j[1] == 1 :
#         print(j,"选了一个")
#     elif j[1] == 2 :
#         print(j,"选了二个")
#     elif j[1] == 3:
#         print(j, "选了三个")
#     elif j[1] == 4:
#         print(j, "选了四个")
# print(type(det))

#
# list = input("随便输入")
# while True:
#     if list.isalnum():
#         print("强度高")
#         exit()

# name_list = ["zhangsan", "lisi", "wangwu", "maliu"]
# salary = [18000, 16000, 20000, 15000]
# # 问题:找出工资最高的人叫啥?
# list = []
# print(name_list[(salary.index(max((salary))))])

# emp = [["zhangsan", 18000], ["lisi", 16000], ["wangwu", 20000], ["maliu", 15000]]
# for i in range(emp.__len__()):
# print("{}的月收入为{}元".format(emp[i][0].ljust(10," "),emp[i][1]))
#

#
# tv = [
#     "戏说西游记:讲述了西游路上的三角恋.",[
#         "孙悟空:悟空爱上了白骨精......",
#         "唐三藏:唐僧只想取经......",
#         "白骨精:她爱上了唐僧......",
#         ],
#     "穿越三国:王二狗打怪升级修仙史",[
#         "王二狗:开局一把刀,一条狗......",
#         "吕布:看我方天画鸡......",
#         "貂蝉:油腻的师姐,充值998就送!",
#         ],
#     "金瓶梅:你懂的",[
#         "西门大官人:你懂的......",
#         "潘金莲:你懂的......",
#         "武大郎:你懂的......",
#         "武松:你懂的......",
#         ],
#     "大明湖畔:我编不下去了......",[
#         "夏雨荷:xxxxxx",
#         "乾隆:xxxxxx",
#
# ddd = tv.index(ccc)
# print(tv.index(tv))
# # for i in range(5):
# #     print()





