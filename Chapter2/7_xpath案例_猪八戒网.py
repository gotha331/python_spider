# 1.拿到页面源代码
# 2.提取和解析数据

import requests
from lxml import etree

url = "https://xian.zbj.com/search/f/?type=new&kw=sass"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}
resp = requests.get(url=url, headers=headers)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)
# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div/div")

for div in divs:
    price = div.xpath("./div/div[2]/div[2]/i/text()")[0].strip("¥")
    title = "sass".join(div.xpath("./div/div[2]/div[3]/a/text()"))
    com_name = div.xpath("./div/div[1]/div[2]/section[1]/h4/a/text()")[0]
    location = div.xpath("./div/div[1]/div[2]/section[1]/div/span/text()")[0]

    print(title)
