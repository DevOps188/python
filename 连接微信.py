import itchat,pyga
itchat.auto_login(hotReload=True)
user_info = itchat.search_friends("王浩鹏")
user_id = user_info[0]['UserName']
f = "E:\放假.PNG"
if 2 > 1 :
    itchat.send("找不到安装包可以访问139.199.33.99:10080下载一个是环境一个是python工具", toUserName=user_id)
    itchat.send_image(f, toUserName=user_id)
    itchat.send("来自windows的网页微信", toUserName=user_id)