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
        cropped.save(dirct + "05" + str(i + 1).zfill(3) +
                     ("b" if b else "") + ".jpg")


def main():
    dirct = "Images/Pantheon/Divinity/"
    name = "httpcloud3steamusercontentcomugc19066885994334981079D393E35804690CCAA893EA97F7CE795C070241.jpg"
    cut_image(dirct, name, 3, False, (2, 2))


main()
