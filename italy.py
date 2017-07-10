# -*- coding: utf-8 -*-
from PIL import Image

image = Image.open(u'D:\Загрузки\wire.png')
limit = 100
img_new = Image.new("RGB", (limit, limit))

change_dir = {(1, 0): (0, 1), (0, 1): (-1, 0),
              (-1, 0): (0, -1),  (0, -1): (1, 0)}
x, y, n, cnt_twice = 0, 0, 1, 1
direction = (1, 0)
for i in range(10000):
    img_new.putpixel((x, y), image.getpixel((i, 0)))
    if n == limit:
        n = 0
        direction = change_dir[direction]
        if cnt_twice:
            limit -= 1
        cnt_twice ^= 1
    n += 1
    x += direction[0]
    y += direction[1]
img_new.save(u'D:\Загрузки\wire_mod.png', "PNG")
