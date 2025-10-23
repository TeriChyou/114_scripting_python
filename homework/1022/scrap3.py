import requests
import re
import json
from bs4 import BeautifulSoup

# send GET request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
response = requests.get('https://www.books.com.tw/web/sys_saletopb/books/19/?attribute=30&loc=P_0002_021', headers=headers)

# Check if the request is successful
try:
    response.raise_for_status() # 若狀態碼非 2xx，則拋出異常
    soup_lxml = BeautifulSoup(response.text, "lxml")
    print("--- 使用 lxml 解析成功 ---")
except requests.exceptions.HTTPError as err:
    print(f"請求失敗: {err}")
    exit(1) # 使用 exit(1) 表示異常結束並返回錯誤碼

books = soup_lxml.find('div', class_='mod_a clearfix').find_all('li', class_='item')
# using for loop to find each elements in articles
res = []
for i in range(20):
    title = books[i].find('h4').find('a').text
    price = re.findall(r'(\d+)元',books[i].find('li', class_='price_a').get_text(strip=True))[0]
    rank = re.findall(r'(\d+)',books[i].find('p', class_='no_list').get_text(strip=True))[0]
    jsonList = {
        "title": title,
        "price": f"NT${price}",
        "rank": f"{rank}"
    }
    res.append(jsonList)
# print in json format not list (ensure_ascii to prevent dollar symbol become ascii code)
print(json.dumps(res, indent=4, ensure_ascii=False))
    

