# 1.定位到2020必看热片
# 2.从2020必看热片中提取到子页面的链接地址
# 3.请求子页面的链接地址，拿到想要的电影下载地址
import requests
import re

domain = "https://www.dytt89.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

resp = requests.get(url=domain, headers=headers, verify=False)  # verify=False:去掉安全验证
resp.encoding = "gb2312"  # 指定字符集
page_content = resp.text
# print(page_content)

# 拿到ul里面的li
obj1 = re.compile(r"2020必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movieName>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<downloadUrl>.*?)">', re.S)

result1 = obj1.finditer(page_content)
movie_href_list = []
for it in result1:
    ul = it.group('ul')

    # 提取子页面链接：
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面的url地址：域名 + 子页面地址
        movie_href = domain + itt.group('href').strip("/")
        movie_href_list.append(movie_href)  # 把子页面链接保存起来

# print(movie_href_list)

# 提取子页面内容
for movie_href in movie_href_list:
    movie_resp = requests.get(url=movie_href, headers=headers, verify=False)
    movie_resp.encoding = "gb2312"
    movie_content = movie_resp.text
    result3 = obj3.search(movie_content)
    print(result3.group("movieName"))
    print(result3.group("downloadUrl"))

