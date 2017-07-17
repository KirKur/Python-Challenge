# -*- coding: utf-8 -*-
import re


def remove_sp(my_str):
    result = re.split(r'\s+$', my_str)
    return result[0]

array1 = []
array2 = []
# parse text file and divide it into two separate columns:
with open('deltas\delta.txt') as img_text:
    for string in img_text:
        col1, col2 = re.split(r'\s{3}\b', string, 1)
        print(col1, '__', col2)
        array1.append(remove_sp(col1))
        array2.append(remove_sp(col2))

delta1 = open('deltas\delta1.png', 'wb')
delta2 = open('deltas\delta2.png', 'wb')
delta3 = open('deltas\delta3.png', 'wb')

# diff two columns and write 3 png images
ptr1, ptr2 = 0, 0

while ptr1 < len(array1) and ptr2 < len(array2):
    if not array1[ptr1] == array2[ptr2]:
        if array1[ptr1+1] == array2[ptr2]:
            delta1.write(bytes.fromhex(array1[ptr1]))
            ptr1 += 1
        elif array1[ptr1] == array2[ptr2+1]:
            delta2.write(bytes.fromhex(array2[ptr2]))
            ptr2 += 1
        else:
            delta1.write(bytes.fromhex(array1[ptr1]))
            delta2.write(bytes.fromhex(array2[ptr2]))
            ptr1 += 1
            ptr2 += 1
    else:
        delta3.write(bytes.fromhex(array2[ptr2]))
        ptr1 += 1
        ptr2 += 1

delta3.close()
delta2.close()
delta3.close()
