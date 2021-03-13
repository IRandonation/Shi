# coding=utf-8
import re
import random
import sys
import time
import datetime
import threading
from random import choice
import requests
import bs4

def get_url(code=0,):
    """
        投票
        如果因为代理IP不可用造成投票失败，则会自动换一个代理IP后继续投
    """

    headers2 = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-cn",
        "Referer":"https://study.jxeduyun.com/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
        }
    try:
        hz_url = "https://study-api.jxeduyun.com/api/courses/8355/course-likes"   # 某投票网站的地址，这里不用真实的域名
        hz_r = requests.post(hz_url,headers=headers2)
    except requests.exceptions.ConnectionError:
        print("ConnectionError")
        get_url(code)
    else:
        date = datetime.datetime.now().strftime('%H:%M:%S')
        pit="第%s次 [%s]：投票%s " % (code,date,hz_r.text)
        print (pit)


ips = []
for i in range(6000):
   

    # 启用线程，隔1秒产生一个线程，可控制时间加快投票速度 ,time.sleep的最小单位是毫秒
    t1 = threading.Thread(target=get_url,args=(i,))
    t1.start()
    print(i)
    time.sleep(1)

