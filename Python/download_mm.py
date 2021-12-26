import urllib.request
import os
# 2593(max)2646 2454

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def get_page(html):
    a = html.find('page">[')
    b = html.find(']', a, a + 100)

    return html[a + 7:b]


def find_imgs(html):
    img_addrs = []
    a = html.find('查看原图')
    a = html.find('<img src="', a, a + 100)

    while a != -1:
        b = html.find('"', a + 10, a + 100)

        if b != -1:
            c = html.find('支持', b)
            c = html.find('span>', c)
            d = html.find('</span', c)
            if int(html[c + 5:d]) >= 10:# 50(103) 30(198) 20(332) 10(821)
                img_addrs.append(html[a + 10:b])
        else:
            b = a + 100

        a = html.find('查看原图', b)
        a = html.find('<img src="', a, a + 100)

    return img_addrs


def save_imgs(folder, img_addrs, page):
    index = 0
    for each in img_addrs:
        index += 1
        print(each)
        filename = page + '-' + str(index) + '.' + each.split('.')[-1]

        with open(filename, 'wb') as f:
            img = url_open('http:' + each)
            f.write(img)


def next_url(html):
    a = html.find('Older Comments')

    if a == -1:
        return "End"

    b = html.find('#comments"', a, a + 100)

    return 'http:' + html[a + 22:b + 9]


def download_mm(folder = 'xxoo'):
    # os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx/"

    while url != "End":
        print(url)
        html = url_open(url).decode('utf-8')
        page = get_page(html)
        print(page)
        img_addrs = find_imgs(html)
        save_imgs(folder, img_addrs, page)
        url = next_url(html)
    print(url)


if __name__ == '__main__':
    download_mm()
