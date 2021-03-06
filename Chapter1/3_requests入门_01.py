import requests

query = input("请输入一个你喜欢的明星：")

url = f"https://www.sogou.com/web?query={query}"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

resp = requests.get(url, headers=headers)

print(resp)
print(resp.text)  # 拿到页面源代码
