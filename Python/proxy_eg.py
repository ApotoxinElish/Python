import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['175.6.66.48:8888', '59.38.223.150:3128', '113.100.209.125:3128']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('urf-8')

print(html)
