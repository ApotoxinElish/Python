from PIL import Image

file = "D:\\FGO\\002.png"

img = Image.open(file)

out = img.convert("L")

width, height = out.size


zoom = 205 / height * 2
vscale = 0.5

out = out.resize((int(width * zoom), int(height * zoom * vscale)))

width, height = out.size

asciis = "@%#*+=-. "


texts = ""

for row in range(height):
    for col in range(width):
        gray = out.getpixel((col, row))
        texts += asciis[int(gray / 255 * 8)]
    texts += "\n"


with open("asciis.txt", "w") as file:
    file.write(texts)
