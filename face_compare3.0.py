#_*_coding:utf-8_*_
#作者:i73636464
#时间:2020/4/17 8:57
#文件:face_compare2.0.py
#IDE :PyCharm
#D:\pycharm\study\ceshi.jpg
from tkinter import *
import requests
import base64
import re
import json
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
response = requests.get(host)
if response:
    access_token = response.json()['access_token']
def change():
    picture_1 = entry_1.get()
    path_1 = picture_1.replace('\\', '/')
    picture_2 = entry_2.get()
    path_2 = picture_2.replace('\\', '/')
    try:
        img_base(path_1,path_2)
    except:
        text.insert(END, '路径格式错误,请按注意事项检查。')
        # 文本框滚动
        text.see(END)
        # 更新
        text.update()
        # print(response.json())
def img_base(path_1,path_2):
    with open(path_1, "rb") as f:
        # b64encode是编码，b64decode是解码
        base64_data = base64.b64encode(f.read())
        pat_1 = "b'(.*?)'"
        data_1 = re.compile(pat_1,re.S).findall(str(base64_data))[0]
    with open(path_2, "rb") as f:
        base64_data = base64.b64encode(f.read())
        pat_2 = "b'(.*?)'"
        data_2 = re.compile(pat_2,re.S).findall(str(base64_data))[0]
    itme_1 = {}
    itme_1['image'] = data_1
    itme_1['image_type'] = 'BASE64'
    itme_1['face_type'] = 'LIVE'
    itme_1['quality_control'] = 'LOW'
    #print(itme_1)
    itme_2 = {}
    itme_2['image'] = data_2
    itme_2['image_type'] = 'BASE64'
    itme_2['face_type'] = 'LIVE'
    itme_2['quality_control'] = 'LOW'
    #print(itme_2)
    list = []
    list.append(itme_1)
    list.append(itme_2)
    compare(list)

def compare(list):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params = json.dumps(list)
    request_url = request_url + "?access_token=" + access_token
    # print(request_url)
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        proportion = response.json()['result']['score']
        # 显示数据到文本框
        text.insert(END, '人脸相似度:{}%'.format(int(proportion)))
        # 文本框滚动
        text.see(END)
        # 更新
        text.update()
        #print(response.json())

root = Tk()
root.title ('人脸相似度对比')
root.geometry('400x270+550+300')
label_1 = Label(root, text = '路径1:', font = ('宋体',20))
label_1.grid(row = 0,column = 0)
entry_1 = Entry(root,font = ('宋体',20))
entry_1.grid(row = 0,column = 1)
label_2 = Label(root, text = '路径2:', font = ('宋体',20))
label_2.grid(row = 1,column = 0)
entry_2 = Entry(root,font = ('宋体',20))
entry_2.grid(row = 1,column = 1)
text = Text(root,width = 55, height = 6,font = ('宋体',10))
text.insert("insert","注意事项："+"\r\n"+"路径格式：D:\pycharm\picture\XXX.jpg"+"\r\n"+"路径1:已知图片*_*_*路径2:需要对比的图片"+"\r\n"+"路径1与路径2图片路径可以互换*_*哈哈哈"+"\r\n"+"路径最好手动打出并且不能出现python内置函数,例如:反斜杠t、反斜杠1、反斜杠User,为什么不能出现反斜杠User我也不知道。")
text.grid(row = 2,columnspan = 2)
button = Button(root,text = '对  比',font = ('宋体',20),command = change)
button.grid(row = 3,column = 0,sticky = W)
button1 = Button(root,text = '退  出',font =( '宋体',20),command = root.quit)
button1.grid(row = 3,column = 1,sticky = E)
text = Listbox(root, font = ('楷书', 16), width = 35, heigh = 3)
# 定位 columnspan 组件横跨的列数
text.grid(row = 4, columnspan = 2)
root.mainloop()