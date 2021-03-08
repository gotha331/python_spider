# 拿到页面源代码，requests
# 通过re来提取想要的有效信息 re

import requests
import re
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

f = open("douban250.csv", mode="w", encoding="utf-8")

for i in range(10):
    url = f"https://movie.douban.com/top250?start={i * 25}&filter="
    resp = requests.get(url=url, headers=headers)
    page_content = resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)人评价', re.S)

    result = obj.finditer(page_content)
    csvwriter = csv.writer(f)

    for it in result:
        print(it.group("name"))
        print(it.group("year").strip())
        print(it.group("score"))
        print(it.group("num"))

        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())

    print(f"第{i + 1}页over!!!")
    time.sleep(5)

f.close()
