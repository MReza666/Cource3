import urllib.request, urllib.parse, urllib.error
import json
#
url=input('insert URL: ')
if len(url)==0:
    url='http://py4e-data.dr-chuck.net/comments_42.json'
#
print('Retrieving', url)
uhandle = urllib.request.urlopen(url)
data = uhandle.read().decode()
print('Retrieved', len(data), 'characters')
print(data)
js = json.loads(data)
print(js)
comments = js['comments']
print("size:",len(comments))
#
sum = 0
for com in comments:
    val = com['count']
    num = int(val)
    sum += num
print("Sum:",sum)
#
