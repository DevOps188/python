import time,os
an = (int(time.time()-86400))
dir = input("输入目录:")


def fong(a):
    for i in os.listdir(a):
        str = os.path.join(dir,i)
        if os.path.isfile(str):
            if os.stat(str)[-2] - an >= 0 :
                print("{} 是一天内修改文件".format(str))
        elif os.path.isdir(str):
            fong(str)


fong(dir)
