# import requests
# from bs4 import BeautifulSoup
#
# url="https://weather.com/zh-CN/weather/hourbyhour/l/f062d8f788da4f814bc222fe32d99886d990ca01a6b1e16bfeb54412d5c82f63"
#
# resp =requests.get(url)
#
# # print(resp) #<Response [200]>
#
# html = resp.content.decode('utf-8')
#
# soup = BeautifulSoup(html,'html.parser')
#
# tr_list = soup.find_all('')
#
# print(tr_list)

import pandas as pd
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
import datetime
import xlwt

# import time

# 导包

time_date=[]
time_now=[]
temperature=[]
weather=[]
wet=[]
wind=[]
Now_Time=datetime.datetime.now()
# windDirection=[]
# windSpeed=[]

# 存储数据列表，wind相关数据同个span标签内两个字段数据，需要二次筛分 #筛分获得数据为单个字符组成列表，搁置此办法

# driver =webdriver.Chrome(executable_path='chromedriver')
# driver = webdriver.PhantomJS(executable_path=r'E:\Anaconda3\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# Chrome 原生浏览器不适合爬取自动化操作，PhantomJS 内核陈旧不再更新，仅维护

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gup')
driver = webdriver.Chrome(options=options)
#无窗口Chrome

driver.get('https://weather.com/zh-CN/weather/hourbyhour/l/f062d8f788da4f814bc222fe32d99886d990ca01a6b1e16bfeb54412d5c82f63')
#江宁_天气

resp_text=driver.page_source
page_html=etree.HTML(resp_text)

# time.sleep(10)

time_date=page_html.xpath('//h3[starts-with(@id,"currentDateId")]')

num = 0
leftHour_today=23-Now_Time.hour
for i in time_date:
    print(i.text)
    time_now = i.xpath('//details/summary/div/div/h2/text()')
    temperature = i.xpath('//details/summary/div/div/div[1]/span/text()')
    weather = i.xpath('//details/summary/div/div/div[2]/span/text()')
    wet = i.xpath('//details/summary/div/div/div[3]/span/text()')
    wind = i.xpath('//details/summary/div/div/div[4]/span/text()')


    # for t in range(int((len(wind)/2)-1)):
    #     # print(wind[2*(t-1)])
    #     windDirection += wind[2*(t-1)]
    #     # print(wind[2*t-1])
    #     windSpeed += wind[2*t-1]

    if num == 0:
        # print(time_now)
        # print(temperature)
        # print(weather)
        # print(wet)
        # print(wind)
        # print(len(wind)) #96

        for j in range(leftHour_today):
            print(time_now[j])
            print(temperature[j])
            print(weather[j])
            print(wet[j])
            print(wind[2*j])
            print(wind[2*j-1])
            # print(wind[j])

    elif num == 1:
        for j in range(24):
            print(time_now[j+leftHour_today])
            print(temperature[j + leftHour_today])
            print(weather[j+ leftHour_today])
            print(wet[j+ leftHour_today])
            print(wind[2 * (j+ leftHour_today)])
            print(wind[2 * (j+ leftHour_today) - 1])
            # print(wind[j+leftHour_today])
    elif num == 2:
        for j in range(Now_Time.hour+1):
            print(time_now[j+leftHour_today+24])
            print(temperature[j+leftHour_today+24])
            print(weather[j+leftHour_today+24])
            print(wet[j+leftHour_today+24])
            print(wind[2 * (j+leftHour_today+24)])
            print(wind[2 * (j+leftHour_today+24) - 1])
            # print(wind[j+leftHour_today+24])

    num += 1
driver.quit()

Objects=[time_now,temperature,weather,wet,wind,time_date]
Names=['time_now','temperature','weather','wet','windDirection','windSpeed']
# Names=['time_now','temperature','weather','wet','wind']

workbook =xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet')
# num_auto=0
for i in range(6):
    worksheet.write(0,i,Names[i])
    for j in range(48):
        if i < 4:
            worksheet.write(j + 1, i, Objects[i][j])
        elif i == 4:
            worksheet.write(j + 1, 4, Objects[4][2*j])
            worksheet.write(j + 1, 5, Objects[4][2*j+1])
            # worksheet.write(j + 1, 4, Objects[4][j])

    # num_auto+=1

Book_Name_01=str(Now_Time.date())+'_'+str(Now_Time.timestamp())+'WeatherHourly.xls'
Book_Name_02=str(Now_Time.date())+'_'+str(Now_Time.timestamp())+'WeatherHourly.csv'
workbook.save(Book_Name_01)
data = pd.read_excel(Book_Name_01,'sheet',index_col=0)
data.to_csv(Book_Name_02,encoding='utf-8')












