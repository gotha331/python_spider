import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
# print(resp.text)

f = open("今日菜价.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 2.从bs对象中查找数据
# find(标签，属性=值)
# find_all(标签，属性=值)
# table = page.find("table", class_="hq_table")
table = page.find("table", attrs={"class": "hq_table"})
print(table)
trs = table.find_all("tr")[1:]
for tr in trs:  # 每一行
    tds = tr.find_all("td")  # 拿到每一行中的所有td
    name = tds[0].text  # .text 表示拿到被标签标记的内容
    low_price = tds[1].text  # .text 表示拿到被标签标记的内容
    avg_price = tds[2].text  # .text 表示拿到被标签标记的内容
    high_price = tds[3].text  # .text 表示拿到被标签标记的内容
    specification = tds[4].text  # .text 表示拿到被标签标记的内容
    kind = tds[5].text  # .text 表示拿到被标签标记的内容
    date = tds[6].text  # .text 表示拿到被标签标记的内容

    # print(name, low_price, avg_price, high_price, specification, kind, date)
    csvwriter.writerow([name, low_price, avg_price, high_price, specification, kind, date])

f.close()
print("over !!!")
