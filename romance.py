import requests

cookies = {'eat': 'yes'}
print(cookies)

r = requests.get('http://www.pythonchallenge.com/pc/return/romance.html', auth=('huge', 'file'),cookies=cookies)

print(r.text)
print(r.cookies)
print(r.content)
print(r.json)
