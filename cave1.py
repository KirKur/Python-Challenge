# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

image = Image.open(u'D:\Загрузки\cave.jpg')
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

img_new = Image.new("RGB", (width / 2, height / 2))
draw = ImageDraw.Draw(img_new)  # Создаем инструмент для рисования.

for i in range(height):
    for j in range(width):
        even = i % 2 == 0 and j % 2 == 0
        odd = i % 2 != 0 and j % 2 != 0
        if even or odd:
            a = pix[j, i][0]
            b = pix[j, i][1]
            c = pix[j, i][2]
            if even:
                y = j / 2
            else:
                y = (j - 1) / 2
            draw.point((y, i), (a, b, c))

img_new.save(u'D:\Загрузки\cave_mod.jpg', "JPEG")
del draw
