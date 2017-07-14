# -*- coding: utf-8 -*-
import re

delta1 = open("deltas\delta1.txt", 'w')
delta2 = open("deltas\delta2.txt", 'w')


def remove_sp(my_str):
    result = re.split(r'\s+$', my_str)
    return result[0]

array1 = []
array2 = []
array2_delta = []
array1_delta = []
array3_both = []
with open('deltas\delta.txt') as img_text:
    for string in img_text:
        result = re.search(r'\s{3}\w', string)
        beg = result.start()
        end = result.end()
        delta1.write((string[:beg]) + '\n')
        array1.append(remove_sp(string[:beg]))
        array2.append(remove_sp(string[end-1:]))
        delta2.write((string[end-1:]))
delta1.close()
delta2.close()

print(len(array1))
print(len(array2))


with open("deltas\delta1_array.txt", 'w') as delta_mod:
    delta_mod.write("89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00\n")
    for item in array1:
        if item not in array2:
            delta_mod.write(item +'\n')


ptr1, ptr2 = 0, 0
'''
for i, (item1, item2) in enumerate (zip(array1, array2)):
    if item1 == item2:
        array_delta.append(item1)
        print(i+1)
'''


while ptr1 < len(array1) and ptr2 < len(array2):
    print(ptr1, ptr2)
    if not array1[ptr1] == array2[ptr2]:
        if (array1[ptr1+1] == array2[ptr2]):
            array1_delta.append(array1[ptr1])
            ptr1 += 1
        elif (array1[ptr1] == array2[ptr2+1]):
            array2_delta.append(array2[ptr2])
            ptr2 += 1
        else:
            array1_delta.append(array1[ptr1])
            ptr1 += 1
            array2_delta.append(array2[ptr2])
            ptr2 += 1
    else:
        array3_both.append(array1[ptr1])
            #exit()
    ptr1 += 1
    ptr2 += 1


byte_list1 = []
byte_list2 = []
byte_list3 = []
byte_list_delta = []

with open("deltas\delta1_array.txt", 'r') as delta_array:
    for string in delta_array:
        byte_list_delta += remove_sp(string).split(' ')

for item in array1_delta:
    byte_list1 += remove_sp(item).split(' ')


for item in array2_delta:
    byte_list2 += remove_sp(item).split(' ')

for item in array3_both:
    byte_list3 += remove_sp(item).split(' ')

with open('deltas\delta1.jpg', 'wb') as delta1:
    for my_byte in byte_list1:
        delta1.write(bytes.fromhex(my_byte))

with open('deltas\delta2.jpg', 'wb') as delta1:
    for my_byte in byte_list2:
        delta1.write(bytes.fromhex(my_byte))

with open('deltas\delta3.jpg', 'wb') as delta3:
    for my_byte in byte_list3:
        delta3.write(bytes.fromhex(my_byte))