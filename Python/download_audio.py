import urllib.request
import os
# 2225(max)


page = 1

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def find_imgs(html):
    img_addrs = []
    a = html.find('title="No.')

    while a != -1:
        c = html.find('" href', a)
        d = html[a + 10:c].zfill(4)
        a = html.find('23747390/', a, a + 100)
        b = html.find('">', a, a + 100)

        if b != -1:
            img_addrs.append((html[a + 9:b], d))
            print(html[a + 9:b])
        else:
            b = a + 100

        a = html.find('title="No.', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        # global number
        # number += 1
        number = each[1]
        print(number)
        # filename = '上海单声部视唱教程第' + str(number).zfill(3) + '条.m4a'
        filename = 'No.' + number + '.m4a'
        html = url_open('https://www.ximalaya.com/revision/play/v1/audio?id=' + each[0] + '&ptype=1').decode('utf-8')
        a = html.find('https')
        b = html.find('.m4a', a)
        addr = html[a:b + 4]

        with open(filename, 'wb') as f:
            img = url_open(addr)
            f.write(img)


def next_url(html):
    global page
    page += 1
    return 'https://www.ximalaya.com/yinyue/23747390/p' + str(page) + '/'


def download_audio(folder = 'audio'):
    # os.mkdir(folder)
    os.chdir(folder)
    url = "https://www.ximalaya.com/yinyue/23747390/"

    
    while url != "End":
        html = url_open(url).decode('utf-8')
        img_addrs = find_imgs(html)
        save_imgs(folder, img_addrs)
        print('save imgs success')
        url = next_url(url)

    print(url)


if __name__ == '__main__':
    download_audio()
