import requests
from bs4 import BeautifulSoup
import pandas as pd

# 目標網址
url = "https://popolist999.blogspot.com/2021/06/google.html"

# 發送請求
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到表格
table = soup.find('table')

# 提取表格標頭
headers = []
if table.find('th'):
    headers = [th.text.strip() for th in table.find_all('th')]
else:
    # 如果沒有 <th>，嘗試使用第一列的 <td> 作為表頭
    first_row = table.find('tr')
    headers = [td.text.strip() for td in first_row.find_all('td')]

# 提取表格內容
data = []
for row in table.find_all('tr'):
    cells = [cell.text.strip() for cell in row.find_all('td')]
    # 只收集列數與表頭一致的行
    if len(cells) == len(headers):
        data.append(cells)

# 如果沒有資料，給出提示
if not data:
    print("無法找到有效的表格數據。請檢查網頁結構。")
else:
    # 存為 DataFrame
    df = pd.DataFrame(data, columns=headers)

    # 保存為 CSV
    df.to_csv("table_data.csv", index=False)
    print("表格已保存為 table_data.csv")
