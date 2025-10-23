import requests
import re

# send GET request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
response = requests.get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html', headers=headers)

# Check if the request is successful
try:
    response.raise_for_status() # 若狀態碼非 2xx，則拋出異常
    print("Request 成功")
    # 3. 解析 HTML
    pattern = re.findall(r'(\£\d+\.\d+)', response.text)
    print(pattern)
except requests.exceptions.HTTPError as err:
    print(f"請求失敗: {err}")
    exit(1) # 使用 exit(1) 表示異常結束並返回錯誤碼

