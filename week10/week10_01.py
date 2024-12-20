import numpy as np
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import datetime
shops = []

# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

for i in range(1, 51):
    url = f"https://www.hollys.co.kr/store/korea/korStore.do?pageNo={i}&sido=&gugun=&store="
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr') # 10
    for tr in trs:
        tds = tr.find_all('td')
        shop_name = tds[1].string # 매장이름
        shop_addr = tds[3].string  # 주소
        shop_phone = tds[5].string  # 전화번호

        shops.append([shop_name, shop_addr, shop_phone, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]) # 2d array

hollys_df = pd.DataFrame(shops, columns=['매장이름', '주소', '전화번호', '일시'])
hollys_df.to_csv('hollys_data.csv', mode='w', encoding='CP949')