import requests
import re
import os

image = "image"
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}
url = "https://blog.csdn.net/weixin_44333889?type=blog"
response = requests.get(url=url, headers=headers)
response.encoding = 'GBK'
response.encoding = 'utf-8'
print(response.request.headers)
print(response.status_code)

t = '<img src="(.*?)" alt="(.*?)" width="160" height="120">'

result = re.findall(t, response.text)

for img in result:
    print(img)
    res = requests.get(img[0])
    print(res.status_code)
    s = img[0].split(".")[-1]
    with open(image + '/' + img[1] + '.' + s, mode='wb') as file:
        file.write(res.content)
