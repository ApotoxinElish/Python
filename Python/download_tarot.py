import urllib.request
import os
# 2225(max)

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def find_imgs(html):
    img_addrs = []
    a = html.find('//tarotator.com/wp-content/uploads/')

    while a != -1:
        b = html.find('.jpg" title="Link', a, a + 100)

        if b != -1:
            img_addrs.append(html[a:b + 4])
            print(html[a:b + 4])
        else:
            b = a + 100

        a = html.find('//tarotator.com/wp-content/uploads/', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]

        with open(filename, 'wb') as f:
            img = url_open('http:' + each)
            f.write(img)


def next_url(html):
    a = html.find('attachment"><a href=')

    if a == -1:
        return "End"

    b = html.find('/" title', a, a + 200)
    print(html[a + 27:b + 1])

    return 'http:' + html[a + 27:b + 1]


def download_mm(folder = 'D:\\Board game\\Tarot'):
    # os.mkdir(folder)
    os.chdir(folder)
    url = "https://tarotator.com/the-rider-waite-smith-tarot-deck/tarot-rider-waite-0-the-fool/"

    while url != "End":
        html = url_open(url).decode('utf-8')
        img_addrs = find_imgs(html)
        save_imgs(folder, img_addrs)
        print('save imgs success')
        url = next_url(html)

    print(url)


if __name__ == '__main__':
    download_mm()
