import requests
import re
import json
from bs4 import BeautifulSoup

# send GET request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
response = requests.get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html', headers=headers)

# Check if the request is successful
try:
    response.raise_for_status() # 若狀態碼非 2xx，則拋出異常
    soup_lxml = BeautifulSoup(response.text, "lxml")
    print("--- 使用 lxml 解析成功 ---")
except requests.exceptions.HTTPError as err:
    print(f"請求失敗: {err}")
    exit(1) # 使用 exit(1) 表示異常結束並返回錯誤碼

articles = soup_lxml.find_all('article', class_='product_pod')
# using for loop to find each elements in articles
res = []
for i in range(len(articles)):
    title = articles[i].find('h3').find('a').get('title')
    # to remove the Â symbol idk why there's such weird stuff
    price = re.findall(r'(\£\d+\.\d+)', articles[i].find('p', class_='price_color').text)[0] 
    rating = articles[i].find('p', class_='star-rating').get('class')[1]
    jsonList = {
        "title": title,
        "price": price,
        "rating": rating
    }
    res.append(jsonList)
# print in json format not list (ensure_ascii to prevent dollar symbol become ascii code)
print(json.dumps(res, indent=4, ensure_ascii=False))
    

