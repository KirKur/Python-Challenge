# -*- coding: utf-8 -*-


image_gfx = open(u'D:\Загрузки\\evil2.gfx', 'rb')

for i in range(5):
    print i
    image_parsed = open(u'D:\Загрузки\\evil_parsed' + str(i) + '.png', 'wb')
    j = 0
    n = 0
    s = image_gfx.read(1)
    while s:  # when EOF s == empty string (i.e. NONE)
        if n % 5 == i:
            image_parsed.write(s)
        n += 1
        s = image_gfx.read(1)
    image_parsed.close()
    image_gfx.seek(0)

image_gfx.close()
