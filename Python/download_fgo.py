import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    
    response = urllib.request.urlopen(req)
    html = response.read()

    return html

def find_page(html, start):
    a = html.find(start)
    if start == 'graph-1' and a == -1:
        a = html.find('class="image"')

    if a == -1:
        return -1

    b = html.find('href=', a) + 6
    c = html.find('"', b)

    return 'https://fgo.wiki' + html[b:c]


def save_img(img_addr, num):
    filename = str(num).zfill(3) + '-2.' + img_addr.split('.')[-1]
    with open(filename, 'wb') as f:
        img = url_open(img_addr)
        f.write(img)


def download_fgo(folder = 'D:/FGO'):

    os.chdir(folder)
    url = "https://fgo.wiki/w/%E7%8E%9B%E4%BF%AE%C2%B7%E5%9F%BA%E5%88%97%E8%8E%B1%E7%89%B9"
    num = 1
    
    while url != -1:
        html = url_open(url).decode('utf-8')
        page_url = find_page(html, 'graph-1')
        url = find_page(html, 'No.' + str(num + 1).zfill(3))
        html = url_open(page_url).decode('utf-8')
        img_addr = find_page(html, 'fullMedia')
        save_img(img_addr, num)
        print(img_addr)
        num += 1

if __name__ == '__main__':
    download_fgo()
