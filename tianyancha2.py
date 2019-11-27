# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:44:43 2019

@author: dhx
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:53:58 2019
读取文件循环输入
@author: dhx
"""
import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import time
import urllib
import random
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver import Chrome

import  pandas  as pd
def get_user_agent():
    user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
    uer_agent = random.choice(user_agent_list)
    return uer_agent
 
def get_ip():
    list = ["112.1.22.111", "200.34.98.11", "99.200.23.10","122.234.143.15","122.234.143.17","122.234.143.63",'1.0.1.0',
'1.0.2.0',
'1.0.8.0',
'1.0.32.0',
'1.1.0.0',
'1.1.2.0',
'1.1.4.0',
'1.1.8.0',
'1.1.16.0',
'1.1.32.0',
'1.2.0.0',
'1.2.2.0',
'1.2.5.0',
'1.2.6.0',
'1.2.8.0',
'1.2.16.0',
'1.2.32.0',
'1.2.64.0',
'1.3.0.0',
'1.4.1.0',
'1.4.2.0',
'1.4.4.0',
'1.4.8.0',
'1.4.16.0',
'1.4.32.0',
'1.4.64.0',
'1.8.0.0',
'1.8.64.0',
'1.8.96.0',
'1.8.100.0',
'1.8.112.0',
'1.8.128.0',
'1.8.144.0',
'1.8.148.0',
'1.8.154.0',
'1.8.156.0',
'1.8.160.0',
'1.8.192.0',
'1.8.224.0',
'1.8.244.0',
'1.8.248.0',
'1.10.0.0',
'1.10.8.0',
'1.10.11.0',
'1.10.12.0',
'1.10.16.0',
'1.10.32.0',
'1.10.64.0',
'1.12.0.0',
'1.24.0.0',
'1.45.0.0',
'1.48.0.0',
'1.56.0.0',
'1.68.0.0',
'1.80.0.0',
'1.116.0.0',
'1.180.0.0',
'1.184.0.0',
'1.188.0.0',
'1.192.0.0',
'1.202.0.0',
'1.204.0.0',
'1.213.105.0',
'12.118.130.0',
'12.126.40.0',
'14.0.0.0',
'14.0.12.0',
'14.1.0.0',
'14.1.24.0',
'14.1.108.0',
'14.16.0.0',
'14.102.128.0',
'14.102.180.0',
'14.103.0.0',
'14.104.0.0',
'14.112.0.0',
'14.130.0.0',
'14.134.0.0',
'14.144.0.0',
'14.192.56.0',
'14.192.76.0',
'14.196.0.0',
'14.204.0.0',
'14.208.0.0',
'20.134.160.0',
'20.139.160.0',
'27.0.128.0',
'27.0.160.0',
'27.0.188.0',
'27.8.0.0',
'27.16.0.0',
'27.34.232.0',
'27.36.0.0',
'27.40.0.0',
'27.50.40.0',
'27.50.128.0',
'27.54.72.0',
'27.54.152.0',
'27.54.192.0',
'27.98.208.0',
'27.98.224.0',
'27.99.128.0',
'27.103.0.0',
'27.106.128.0',
'27.106.204.0',
'27.109.32.0',
'27.109.124.0',
'27.112.0.0',
'27.112.80.0',
'27.112.112.0',
'27.113.128.0',
'27.115.0.0',
'27.116.44.0',
'27.121.72.0',
'27.121.120.0',
'27.128.0.0',
'27.131.220.0',
'27.144.0.0',
'27.148.0.0',
'27.152.0.0',
'27.184.0.0',
'27.192.0.0',
'27.224.0.0',
'36.0.0.0',
'36.0.16.0',
'36.0.32.0',
'36.0.64.0',
'36.0.128.0',
'36.1.0.0',
'36.4.0.0',
'36.16.0.0',
'36.32.0.0',
'36.36.0.0',
'36.37.0.0',
'36.37.36.0',
'36.37.39.0',
'36.37.40.0',
'36.37.48.0',
'36.40.0.0',
'36.48.0.0',
'36.51.0.0',
'36.51.128.0',
'36.51.192.0',
'36.51.224.0',
'36.51.240.0',
'36.51.248.0',
'36.51.252.0',
'36.56.0.0',
'36.96.0.0',
'36.128.0.0',
'36.192.0.0',
'36.248.0.0',
'36.254.0.0',
'36.255.116.0',
'36.255.128.0',
'36.255.164.0',
'36.255.172.0',
'36.255.176.0',
'39.0.0.0',
'39.0.2.0',
'39.0.4.0',
'39.0.8.0',
'39.0.16.0',
'39.0.32.0',
'39.0.64.0',
'39.0.128.0',
'39.64.0.0',
'39.96.0.0',
'39.104.0.0',
'39.108.0.0',
'39.128.0.0',
'40.0.176.0',
'40.0.247.0',
'40.0.248.0',
'40.0.252.0',
'40.0.255.0',
'40.72.0.0',
'40.125.128.0',
'40.126.64.0',
'40.198.10.0',
'40.198.16.0',
'40.198.24.0',
'40.251.225.0',
'40.251.227.0',
'42.0.0.0',
'42.0.8.0',
'42.0.16.0',
'42.0.24.0',
'42.0.32.0',
'42.0.128.0',
'42.0.160.0',
'42.0.176.0',
'42.0.184.0',
'42.0.186.0',
'42.0.188.0',
'42.0.192.0',
'42.0.208.0',
'42.0.216.0',
'42.0.220.0',
'42.0.223.0',
'42.0.224.0',
'42.1.0.0',
'42.1.32.0',
'42.1.48.0',
'42.1.56.0',
'42.4.0.0',
'42.48.0.0',
'42.56.0.0',
'42.62.0.0',
'42.62.128.0',
'42.62.160.0',
'42.62.180.0',
'42.62.184.0',
'42.63.0.0',
'42.80.0.0',
'42.83.64.0',
'42.83.80.0',
'42.83.88.0',
'42.83.96.0',
'42.83.128.0',
'42.83.134.0',
'42.83.140.0',
'42.83.142.0',
'42.83.144.0',
'42.83.160.0',
'42.83.192.0',
'42.84.0.0',
'42.88.0.0',
'42.96.64.0',
'42.96.96.0',
'42.96.108.0',
'42.96.112.0',
'42.96.128.0',
'42.97.0.0',
'42.99.0.0',
'42.99.64.0',
'42.99.96.0',
'42.99.112.0',
'42.99.120.0',
'42.100.0.0',
'42.120.0.0',
'42.122.0.0',
'42.123.0.0',
'42.123.36.0',
'42.123.40.0',
'42.123.48.0',
'42.123.64.0',
'42.123.128.0',
'42.123.160.0',
'42.123.164.0',
'42.123.166.0',
'42.123.168.0',
'42.123.176.0',
'42.123.192.0',
'42.128.0.0',
'42.156.0.0',
'42.156.36.0',
'42.156.40.0',
'42.156.48.0',
'42.156.64.0',
'42.156.128.0',
'42.157.0.0',
'42.158.0.0',
'42.160.0.0',
'42.176.0.0',
'42.184.0.0',
'42.186.0.0',
'42.187.0.0',
'42.187.64.0',
'42.187.96.0',
'42.187.112.0',
'42.187.120.0',
'42.187.128.0',
'42.192.0.0',
'42.201.0.0',
'42.202.0.0',
'42.204.0.0',
'42.208.0.0',
'42.224.0.0',
'42.240.0.0',
'42.242.0.0',
'42.244.0.0',
'42.248.0.0',
'43.224.12.0',
'43.224.24.0',
'43.224.44.0',
'43.224.52.0',
'43.224.56.0',
'43.224.64.0',
'43.224.72.0',
'43.224.80.0',
'43.224.100.0',
'43.224.144.0',
'43.224.160.0',
'43.224.176.0',
'43.224.184.0',
'43.224.200.0',
'43.224.208.0',
'43.224.216.0',
'43.224.240.0',
'43.225.76.0',
'43.225.84.0',
'43.225.120.0',
'43.225.180.0',
'43.225.184.0',
'43.225.208.0',
'43.225.216.0',
'43.225.224.0',
'43.225.240.0',
'43.225.252.0',
'43.226.32.0',
'43.226.64.0',
'43.226.96.0',
'43.226.112.0',
'43.226.120.0',
'43.226.128.0',
'43.226.160.0',
'43.226.236.0',
'43.226.240.0',
'43.227.0.0',
'43.227.8.0',
'43.227.32.0',
'43.227.64.0',
'43.227.104.0',
'43.227.136.0',
'43.227.144.0',
'43.227.152.0',
'43.227.160.0',
'43.227.176.0',
'43.227.188.0',
'43.227.192.0',
'43.227.232.0',
'43.227.248.0',
'43.228.0.0',
'43.228.64.0',
'43.228.76.0',
'43.228.100.0',
'43.228.116.0',
'43.228.132.0',
'43.228.136.0',
'43.228.148.0',
'43.228.152.0',
'43.228.188.0',
'43.229.40.0',
'43.229.56.0',
'43.229.96.0',
'43.229.136.0',
'43.229.168.0',
'43.229.176.0',
'43.229.192.0',
'43.229.216.0',
'43.229.232.0',
'43.230.20.0',
'43.230.32.0',
'43.230.68.0',
'43.230.72.0',
'43.230.84.0',
'43.230.124.0',
'43.230.220.0',
'43.230.224.0',
'43.231.12.0',
'43.231.32.0',
'43.231.80.0',
'43.231.96.0',
'43.231.136.0',
'43.231.144.0',
'43.231.160.0',
'43.231.176.0',
'43.236.0.0',
'43.238.0.0',
'43.239.0.0',
'43.239.32.0',
'43.239.48.0',
'43.239.116.0',
'43.239.120.0',
'43.239.172.0',
'43.240.0.0',
'43.240.56.0',
'43.240.68.0',
'43.240.72.0',
'43.240.84.0',
'43.240.124.0',
'43.240.128.0',
'43.240.136.0',
'43.240.156.0',
'43.240.160.0',
'43.240.192.0',
'43.240.240.0',
'43.241.0.0',
'43.241.16.0',
'43.241.48.0',
'43.241.76.0',
'43.241.80.0',
'43.241.112.0',
'43.241.168.0',
'43.241.176.0',
'43.241.184.0',
'43.241.208.0',
'43.241.224.0',
'43.241.240.0',
'43.241.248.0',
'43.242.8.0',
'43.242.16.0',
'43.242.48.0',
'43.242.64.0',
'43.242.72.0',
'43.242.80.0',
'43.242.96.0',
'43.242.144.0',
'43.242.160.0',
'43.242.180.0'
]
    ip = random.choice(list)
    return ip
def get_re(urls):
    for i in range(len(urls)):
        re = urls[i]
    return re
#TYCID=020c3ff0dde411e9a59da3aa3f774194; undefined=020c3ff0dde411e9a59da3aa3f774194; ssuid=3730796414; _ga=GA1.2.735910374.1569230699; _gid=GA1.2.1695011729.1570684430; RTYCID=fa993cc601444e0a9f427d33e1de6af3; CT_TYCID=3ca01612cda14aad8977852ceec69177; aliyungf_tc=AQAAAJlb0xtbZwAA8lKt3iO6lvWPHZlK; csrfToken=XZIBAqFpWenrpyY1ifOGERbr; jsid=SEM-BAIDU-PZ1907-SY-000100; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1569230699,1570684430,1570754283; bannerFlag=true; token=d6a69cf2e4dd45688067b7ec2896bedd; _utm=848bd904769c41f3a749cd3576d33301; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%25BB%2584%25E5%2593%2581%25E6%25B2%2585%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522400%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzg2MDc0NzM2MCIsImlhdCI6MTU3MDc2NDYyMiwiZXhwIjoxNjAyMzAwNjIyfQ.8ZS6N6VLf5PKGcEx83mCgL3Lp7EwJ8MF4VpdNMrQVq_UqkLU7LrRizSMMvZFDpEu03kFwFbDKpo5b0cnrVWtlg%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217860747360%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzg2MDc0NzM2MCIsImlhdCI6MTU3MDc2NDYyMiwiZXhwIjoxNjAyMzAwNjIyfQ.8ZS6N6VLf5PKGcEx83mCgL3Lp7EwJ8MF4VpdNMrQVq_UqkLU7LrRizSMMvZFDpEu03kFwFbDKpo5b0cnrVWtlg; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1570788829; _gat_gtag_UA_123487620_1=1; cloud_token=43f2087e4b714dd689c394f966704ece; cloud_utm=34b223519e054538b8a46610673b7e19 
def craw(url):
#    re = r'https://www.tianyancha.com/search?key='+key_word
#    urls = ['https://www.tianyancha.com/company/5227844','https://www.tianyancha.com/company/3018725013',
#            'https://www.tianyancha.com/company/1091454121','https://www.tianyancha.com/company/809076978',
#            'https://www.tianyancha.com/company/2561694985','https://www.tianyancha.com/company/304234705']
    headers = {
            'Host':'www.tianyancha.com',
            'Connection': 'keep-alive',
            'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            
            'User-Agent':get_user_agent(),
            'Referer': get_re(urls),
            'X-Forwarded-For': get_ip(),
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cookie':r'TYCID=020c3ff0dde411e9a59da3aa3f774194; undefined=020c3ff0dde411e9a59da3aa3f774194; ssuid=3730796414; _ga=GA1.2.735910374.1569230699; jsid=SEM-BAIDU-PZ1907-SY-000100; aliyungf_tc=AQAAAMh5R1Sy3wQA8lKt3tlOCWis+ovI; csrfToken=SEV649jW8i8hW5XyClrdQ2T9; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1571902874,1571985584,1572308660,1574210720; _gid=GA1.2.130824873.1574210720; RTYCID=2d4caaefbe804c24aa97222e417d269c; CT_TYCID=d6530eee66ac4313bc9d2341869f5093; cloud_token=5f154a3c4c3242a9a8f8ffd7f8eb9704; cloud_utm=fd00b309f5e14887adfa591d08acbac6; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1574239646; _gat_gtag_UA_123487620_1=1; token=bac075714c3b4fe08730bf47202eb67b; _utm=ec056e4378b9406f98ea47a3b55791cb; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E9%25BB%2584%25E5%2593%2581%25E6%25B2%2585%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522440%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzg2MDc0NzM2MCIsImlhdCI6MTU3NDIzOTY3NiwiZXhwIjoxNjA1Nzc1Njc2fQ.PVXsdLDUBS_gKcoOhvwmngR1MIHH_9-9sl139mtn2XjlA8texijRLljsb7S2J3jlyi15G0vjLdI6NDqCBLEFHg%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217860747360%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzg2MDc0NzM2MCIsImlhdCI6MTU3NDIzOTY3NiwiZXhwIjoxNjA1Nzc1Njc2fQ.PVXsdLDUBS_gKcoOhvwmngR1MIHH_9-9sl139mtn2XjlA8texijRLljsb7S2J3jlyi15G0vjLdI6NDqCBLEFHg',
            }
  
    for url in urls:
        
        path = r'F:\study\dhx\code\tianYanCha1.xlsx'
        try:
            df1 = pd.read_excel(path)
        except:
            df1 = pd.DataFrame(columns=['Company','Phone','Address','info'])
        try:
            response = requests.get(url,headers = headers)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')            
#            com_all_info = soup.find("div",{'class':'detail'})
            company = soup.find('div',class_='header').find("h1",{'class':'name'}).get_text()
                       
            phone = soup.find("div",{'class':'in-block sup-ie-company-header-child-1'}).find_all('span')[1].getText()
            
            info = soup.find("script",{'id':'company_base_info_detail'}).get_text()            
            
            address = soup.find("div",{'class':'auto-folder'}).find('div').getText()
            
#            qy_info = soup.find('div',{'class':'data-content'})
            
#            zhucezijin = qy_info.find('td')[1].getText()
            
#            hangye = qy_info.find('tr')[2].find('td')[3].getText()
            
            df1.loc[df1.shape[0],'Company'] = company
            df1.loc[df1.shape[0]-1,'Phone'] = phone
            df1.loc[df1.shape[0]-1,'Address'] = address
            df1.loc[df1.shape[0]-1,'info'] = info
#            df1.loc[df1.shape[0]-1,'注册资金'] = zhucezijin
#            df1.loc[df1.shape[0]-1,'所属行业'] = hangye
            df1.to_excel(path,index=0)

            print(info)
            print(company)                          
            print(phone)
            print(address) 
#            print(zhucezijin)
#            print(hangye)

        except Exception:
            print('好像被拒绝访问了呢...请稍后再试叭...')
        
if __name__ == '__main__':
    urls = ['https://www.tianyancha.com/company/113279664']
    craw(urls)

#    global name_list
#    global phone_list
#    global address_list
#    global urls
#    global info_list
#    
#    
#    
#    urls = ['https://www.tianyancha.com/company/5227844']
#    name_list=[]
#    phone_list=[] 
#    address_list=[]  
#    info_list = []
#    
#    workbook = xlwt.Workbook()  #创建sheet对象，新建sheet  
#    sheet1 = workbook.add_sheet('企查查数据', cell_overwrite_ok=True)
#    style = xlwt.XFStyle()
#    font = xlwt.Font()
#    font.name = '仿宋'
#    style.font = font
#    name_list1 = ['公司名字','法人电话','地址','简介']
#    for cc in range(0,len(name_list1)):
#        sheet1.write(0,cc,name_list1[cc],style)    
#    data = pd.read_excel('test.xlsx')
#    for url in urls:
#        s1 = craw(url)
#   
#        for i in range(0,len(name_list)):
#            sheet1.write(i+1,0,name_list[i],style)#公司名字
#            sheet1.write(i+1,1,phone_list[i],style)#法人电话
#            sheet1.write(i+1,2,address_list[i],style)
#            sheet1.write(i+1,3,info_list[i],style)
#    workbook.save(r"F:\study\dhx\test1.xls")
#    print('保存完毕~')
#        