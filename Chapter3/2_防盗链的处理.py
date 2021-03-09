# 1.拿到contId
# 2.拿到videoStatus接口返回的json -> srcURL
# 3.对srcURL里面的内容进行修整
# 4.下载视频

import requests
import json

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1722486"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    # 防盗链:溯源 -> 本次请求的上一级是谁
    "Referer": url
}

contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.19248089363780285"

resp = requests.get(url=videoStatusUrl, headers=headers)
# print(resp.json())
# print(json.dumps(resp.json(), indent=4))
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# print(srcUrl)

# 下载视频
with open("a.mp4", "wb") as f:
    f.write(requests.get(srcUrl).content)

f.close()
print("over！！！")
