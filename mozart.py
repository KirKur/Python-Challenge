# -*- coding: utf-8 -*-
import Image

image = Image.open(u'D:\Загрузки\mozart.gif')
image_rgb = image.convert('RGB')
pixels = image_rgb.load()
width = image.size[0]
height = image.size[1]
img_new = Image.new("RGB", (width, height))

new_pixels = []

for j in range(height):
    buff_pixel_row = []
    pixel_row = []
    find_pink = True
    for i in range(width):
        if image_rgb.getpixel((i, j)) == (255, 0, 255):
            find_pink = False
        if find_pink:
            buff_pixel_row.append(image_rgb.getpixel((i, j)))
        else:
            pixel_row.append(image_rgb.getpixel((i, j)))
    new_pixels.append(pixel_row + buff_pixel_row)

for j in range(height):
    for i in range(width):
        img_new.putpixel((i,j), new_pixels[j][i])

img_new.save(u'D:\Загрузки\mozart_shift.png', "PNG")
