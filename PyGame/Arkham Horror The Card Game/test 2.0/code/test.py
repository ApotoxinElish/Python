from PIL import Image


def cut_image(dirct, name, amount, b=False, scale=(10, 7)):
    img = Image.open(dirct + name)
    width = img.size[0] / scale[0]
    height = img.size[1] / scale[1]
    for i in range(amount):
        left = i % scale[0] * width
        upper = i // scale[0] * height
        right = left + width
        lower = upper + height
        cropped = img.crop((left, upper, right, lower))
        cropped.save(dirct + "01" + str(i + 1).zfill(3) +
                     ("b" if b else "") + ".jpg")


def main():
    dirct = "../images/CN/"
    name = "httpcloud3steamusercontentcomugc775107869048626382DA1F5817A4067A74D883201F1AFAC096646A455B.jpg"
    cut_image(dirct, name, 29, False)


main()
