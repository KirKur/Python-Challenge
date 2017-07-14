
import requests
import bz2
from urllib import parse
import urllib.request


def extract_num(my_string):
    num = ""
    for char in my_string:
        if char in '0123456789':
            num += char
    return num
cookies = dict(info='the flowers are on their way')
r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345, cookies=cookies')
print(r.cookies)
print (r.content)
#exit()
temp_answer2 = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
temp_answer = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
temp_answer_Vad = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
if temp_answer2 == temp_answer == temp_answer_Vad:
    print('they are identical!!!')

expr = parse.unquote_to_bytes(temp_answer.replace('+', '%20'))

print(expr)
print(type(expr))
str_ex = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
answer = bz2.decompress(str_ex)
print(answer)
answer = bz2.decompress(expr)
print(answer)
exit()
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
base_urlbusy = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
num_url = "12345"
jump_num = 0
result_bz = ''
while num_url:
    r = requests.get(base_urlbusy + num_url)

    try:
        r.cookies.items()[0][1]
    except:
        break
    result_bz += r.cookies.items()[0][1]
    # print(r.cookies.items()[0][1])
    next_url = base_urlbusy + num_url
    print('Opening... ' + next_url)
    response = urllib.request.urlopen(next_url)
    # print(response.headers.get_content_charset('default'))
    my_string = str(response.read())
    print(my_string)
    if (my_string == "b'Yes. Divide by two and keep going.'"):
        num_url = str(int(num_url) / 2)
    else:
        my_string = my_string[my_string.find("and the next busynothing is"):]
        # print (my_string)
        num_url = extract_num(my_string)
    print(num_url)
    jump_num += 1
    # print(jump_num)

# BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084

print(result_bz)

# print(r.text)
# print(r.cookies)
# print(r.content)
# print(r.json)
