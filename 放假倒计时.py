import time
bb = int(time.mktime(time.strptime("2019-01-27 18:00:00","%Y-%m-%d %H:%M:%S")))
while True:
    s = bb - int(time.time())
    if s == 0:
        break
    else:
        print("距离放假还剩{}天{}时{}分{}秒时间一天天的过 而我只想月薪过万".format(int(s/86400),int(s%86400/3600),int(s%3600/60),int(s%60)))


