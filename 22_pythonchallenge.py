import zlib
import bz2

def bzip_that(data):
    bzip_data = data
    while True:
        print(str(bzip_data[0:1])[2:-1], end='')
        bzip_data = bz2.decompress(bzip_data)
        if bzip_data[0] != 66:
            break
    return bzip_data


def zlib_that(data):
    zlib_data = data
    while True:
        print(' ', end='')
        zlib_data = zlib.decompress(zlib_data,0)
        if zlib_data != 120:
            break
    return zlib_data

with open("readme_idiot/package.pack", 'rb') as cut_pack:
    data = cut_pack.read()
    print(type(data))

print("start")
while data[0] == 66 or data[0] == 120:
    if data[0] == 66:
        data = bzip_that(data)
    elif data[0] == 120:
        data = zlib_that(data)

    if data[0] != 66 and data[0] != 120:
        print('')
     #   print("turning data")
        data = data[::-1]
print('\n')
print(data)

