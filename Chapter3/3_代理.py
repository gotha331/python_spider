import requests

proxies = {
    "http": "http://218.60.8.99:3129"
}

resp = requests.get("http://www.baidu.com",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
