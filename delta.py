# -*- coding: utf-8 -*-
import re

array1 = []
array2 = []
# parse text file and divide it into two separate columns:
with open('deltas\delta.txt') as img_text:
    for string in img_text:
        col1, col2 = re.split(r'\s{3}\b', string, 1)
        array1.append(col1.strip())
        array2.append(col2.strip())

delta1 = open('deltas\delta1.png', 'wb')
delta2 = open('deltas\delta2.png', 'wb')
delta3 = open('deltas\delta3.png', 'wb')

# diff two columns and write 3 png images
ptr1, ptr2 = 0, 0

while ptr1 < len(array1) and ptr2 < len(array2):
    if not array1[ptr1] == array2[ptr2]:
        if array1[ptr1+1] == array2[ptr2]:  # addition in first column
            delta1.write(bytes.fromhex(array1[ptr1]))
            ptr1 += 1
        elif array2[ptr2+1] == array1[ptr1]:  # addition in second column
            delta2.write(bytes.fromhex(array2[ptr2]))
            ptr2 += 1
        else:  # addition in both columns
            delta1.write(bytes.fromhex(array1[ptr1]))
            delta2.write(bytes.fromhex(array2[ptr2]))
            ptr1 += 1
            ptr2 += 1
    else:  # no additions
        delta3.write(bytes.fromhex(array2[ptr2]))
        ptr1 += 1
        ptr2 += 1

delta3.close()
delta2.close()
delta3.close()
