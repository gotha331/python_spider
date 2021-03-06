import requests

url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

s = input("请输入你要翻译的单词：")
data = {
    "kw": s
}

resp = requests.post(url=url, headers=headers, data=data)
print(resp)
print(resp.json())  # 将服务器返回的内容直接处理成json() => dic
