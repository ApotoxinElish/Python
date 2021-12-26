import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def find_imgs(html):
    img_addrs = []
    a = html.find('img src="')

    while a != -1:
        b = html.find('"', a + 10, a + 100)

        if b != -1:
            img_addrs.append(html[a + 9:b])
            print(html[a + 9:b])
        else:
            b = a + 100

        a = html.find('img src="', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]

        with open(filename, 'wb') as f:
            img = url_open('https://arkhamdb.com' + each)
            f.write(img)


def next_url(html):
    a = html.find('class="next"')
    a = html.find('href="', a, a + 100)

    if a == -1:
        print("End")
        exit(0)
        
    b = html.find('"', a + 10, a + 100)
    print(html[a + 6:b])

    return 'https://arkhamdb.com' + html[a + 6:b]


def download_mm(folder = 'Arkham'):
    # os.mkdir(folder)
    os.chdir(folder)
    url = "https://arkhamdb.com/card/01001"

    while True:
        html = url_open(url).decode('utf-8')
        img_addrs = find_imgs(html)
        save_imgs(folder, img_addrs)
        url = next_url(html)
        print(url)


if __name__ == '__main__':
    download_mm()
