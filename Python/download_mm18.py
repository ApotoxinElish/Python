import urllib.request
import os
# 2225(max)

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def find_url(url):
    html = url_open(url).decode('ANSI')
    a = html.find('href="')
    while a != -1:
        b = html.find('.html"', a, a + 100)
        if b != -1:
            url = html[a + 6:b + 5]
            print(url)
            break
        b = a + 100
        a = html.find('href="', b)
    return url


def find_img(url):
    html = url_open(url).decode('ANSI')
    a = html.find(')" src="https')

    while a != -1:
        b = html.find('.jpg"', a, a + 100)

        if b != -1:
            addr = html[a + 8:b + 4]
            print(addr)
            save_img(addr)
            break
        b = a + 100
        a = html.find('img src="//wx', b)



def save_img(addr):
    filename = addr.split('/')[-1]

    with open(filename, 'wb') as f:
        img = url_open(addr)
        f.write(img)


def next_url(html):
    a = html.find('Older Comments')

    if a == -1:
        return "End"

    b = html.find('=#comments"', a, a + 100)
    print(html[a + 22:b + 10])

    return 'http:' + html[a + 22:b + 10]


def download_mm(folder = 'xinggan'):
    # os.mkdir(folder)
    os.chdir(folder)
    url = find_url("https://m.mm131.net/xinggan/")

    find_img(url)

    '''while url != "End":
        html = url_open(url).decode('utf-8')
        img_addrs = find_imgs(html)
        save_imgs(folder, img_addrs)
        url = next_url(html)'''


if __name__ == '__main__':
    download_mm()
