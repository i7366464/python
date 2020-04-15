#_*_coding:utf-8_*_
#作者:i7366464
#时间:2020/4/14 13:33
#文件:天气3.0.py
#IDE :PyCharm

import requests
import json
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header



#def today():

city_id = "所在城市id"   #天气id.xlsx中district_id的6位数字
#    input("请输入城市ID:")
AK = "ak"   #在百度地图开放平台创建项目后会有对应的ak
url = "http://api.map.baidu.com/weather/v1/?district_id=" + str(city_id) + "&data_type=all&ak=" + str(AK)
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
result_news = requests.get(url , headers = headers).text
#print
result_news_josn = json.loads(result_news)
#for i in range(0,5):
result_new = result_news_josn['result']['forecasts']
    #{'text_day': '晴', 'text_night': '晴', 'high': 20, 'low': 2, 'wc_day': '<3级', 'wd_day': '西风', 'wc_night': '<3级', 'wd_night': '西风', 'date': '2020-04-13', 'week': '星期一'}
def tips():
    print('*' * 12)
    print('今天请输入"1"')
    print('明天请输入"2"')
    print('后天请输入"3"')
    print('*' * 12)
def today():
    date = result_new[0]['date']   #日期：2020年4月14日
    week = result_new[0]['week']   #星期：星期二
    text_day = result_new[0]['text_day']   #白天的天气情况
    #text_night = result_new[0]['text_night']   #晚上的天气情况
    high = result_new[0]['high']   #最高气温
    low = result_new[0]['low']   #最低气温
    wd_day = result_new[0]['wd_day']   #白天风向
    wc_day = result_new[0]['wc_day']   #白天风力
    #wd_night = result_new[0]['wd_night']   #晚上风向
    #wc_night = result_new[0]['wc_night']   #晚上风力
    item_i = {}  # 创建一个空字典，储存天气信息
    item_i['日期,星期,天气'] = date, week, str('天气：') + str(text_day)
    item_i['最高气温，最低气温'] = str('最高气温：') + str(high), str('最低气温：') + str(low)
    item_i['风向，风力'] = str('风向：') + str(wd_day), str('风力：') + str(wc_day)
    tuple_i = (item_i['日期,星期,天气'] + item_i['最高气温，最低气温'] + item_i['风向，风力'])
    result_i = ' '.join(tuple_i)
    email(result_i)
    print(result_i)
    #print(' '.join(tuple_i))
def second_day():
    date = result_new[1]['date']  # 日期：2020年4月14日
    week = result_new[1]['week']  # 星期：星期二
    text_day = result_new[1]['text_day']  # 白天的天气情况
    # text_night = result_new[1]['text_night']   #晚上的天气情况
    high = result_new[1]['high']  # 最高气温
    low = result_new[1]['low']  # 最低气温
    wd_day = result_new[1]['wd_day']  # 白天风向
    wc_day = result_new[1]['wc_day']  # 白天风力
    # wd_night = result_new[1]['wd_night']   #晚上风向
    # wc_night = result_new[1]['wc_night']   #晚上风力
    item_i = {}  # 创建一个空字典，储存天气信息
    item_i['日期,星期,天气'] = date, week, str('天气：') + str(text_day)
    item_i['最高气温，最低气温'] = str('最高气温：') + str(high), str('最低气温：') + str(low)
    item_i['风向，风力'] = str('风向：') + str(wd_day), str('风力：') + str(wc_day)
    tuple_i = (item_i['日期,星期,天气'] + item_i['最高气温，最低气温'] + item_i['风向，风力'])
    result_i = ' '.join(tuple_i)
    email(result_i)
    print(result_i)
def third_day():
    date = result_new[2]['date']  # 日期：2020年4月14日
    week = result_new[2]['week']  # 星期：星期二
    text_day = result_new[2]['text_day']  # 白天的天气情况
    # text_night = result_new[2]['text_night']   #晚上的天气情况
    high = result_new[2]['high']  # 最高气温
    low = result_new[2]['low']  # 最低气温
    wd_day = result_new[2]['wd_day']  # 白天风向
    wc_day = result_new[2]['wc_day']  # 白天风力
    # wd_night = result_new[2]['wd_night']   #晚上风向
    # wc_night = result_new[2]['wc_night']   #晚上风力
    item_i = {}  # 创建一个空字典，储存天气信息
    item_i['日期,星期,天气'] = date, week, str('天气：') + str(text_day)
    item_i['最高气温，最低气温'] = str('最高气温：') + str(high), str('最低气温：') + str(low)
    item_i['风向，风力'] = str('风向：') + str(wd_day), str('风力：') + str(wc_day)
    tuple_i = (item_i['日期,星期,天气'] + item_i['最高气温，最低气温'] + item_i['风向，风力'])
    result_i = ' '.join(tuple_i)
    email(result_i)
    print(result_i)
def email(result_i):
    # 用于构建邮件头

    # 发信方的信息：发信邮箱，邮箱授权码
    from_addr = 'xxxxx@163.com'
    password = 'xxxxx'

    # 收信方邮箱
    to_addr = 'xxxxx@qq.com'

    # 发信服务器,smtp_server 需要按照不同的发信邮箱进行更改
    smtp_server = 'smtp.163.com'
    gushi = result_i
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(gushi, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('天气情况')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
if __name__ == '__main__':
    tips()
    date = int(input("请输入时间："))
    if date == 1:
        today()
    if date == 2:
        second_day()
    if date == 3:
        third_day()

