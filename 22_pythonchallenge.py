import zlib
import bz2


def inflate(data):
    inflated = zlib.decompress(data, 0)
    return inflated


def bzip_that(data):
    bzip_data = data
    while True:
        print(str(bzip_data[0:1])[2:-1], end='')
        bzip_data = bz2.decompress(bzip_data)
        if bzip_data[0] != 66:
            break
    return bzip_data


def inflate_that(data):
    inflate_data = data
    while True:
        print(' ', end='')
        inflate_data = inflate(inflate_data)
        if inflate_data != 120:
            break
    return inflate_data

with open("readme_idiot/package.pack", 'rb') as cut_pack:
    data = cut_pack.read()
    print(type(data))

print("start")
while data[0] == 66 or data[0] == 120:
    if data[0] == 66:
        data = bzip_that(data)
    elif data[0] == 120:
        data = inflate_that(data)

    if data[0] != 66 and data[0] != 120:
        print('')
     #   print("turning data")
        data = data[::-1]
print('\n')
print(data)

