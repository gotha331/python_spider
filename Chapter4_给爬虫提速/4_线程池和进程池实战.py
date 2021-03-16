# 目标：爬取北京新发地全部菜价
# 1.如何提取单个页面的数据
# 2.上线程池，多个页面同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # trs = table.xpath("./tr")[1:]
    trs = table.xpath("./tr[position() > 1]")

    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做简单的处理：\\ / 去掉
        # 生成器
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # 把数据存放在文件中
        csvwriter.writerow(txt)

    print(url, "提取完毕!")


if __name__ == '__main__':
    # download_one_page("http://www.xinfadi.com.cn/marketanalysis/0/list/2.shtml")
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page, url=f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

    # 等待线程池中的任务全部执行完毕，才继续执行（守护）
    print("全部下载完毕！")
