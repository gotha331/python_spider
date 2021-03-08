# 1.拿到主页面的源代码，然后提取到子页面的链接地址， href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img -> src
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import os
import time

# 创建一个文件夹，保存所有的图片
if not os.path.exists('./umei'):
    os.mkdir('./umei')

main_url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

resp = requests.get(url=main_url, headers=headers)
resp.encoding = "utf-8"

# 把页面源码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
a_list = main_page.find("div", attrs={"class": "TypeList"}).find_all("a")

for a in a_list:
    href = a.get("href")  # 直接通过get就可以拿到属性的值
    # 拿到子页面的源代码
    child_page_resp = requests.get(url=href, headers=headers)
    child_page_resp.encoding = "utf-8"

    # 解析大图地址
    child_page = BeautifulSoup(child_page_resp.text, "html.parser")
    image_body = child_page.find("div", attrs={"class": "ImageBody"})
    img_src = image_body.find("img").get("src")
    # 下载图片
    img_data = requests.get(url=img_src, headers=headers).content
    img_name = img_src.split("/")[-1]
    img_path = './umei/' + img_name
    with open(img_path, mode="wb") as f:
        f.write(img_data)
        print(img_name, "下载成功！！")
    time.sleep(2)

print('over !!!')
