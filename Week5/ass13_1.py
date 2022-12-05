import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
#
url=input('insert URL: ')
if len(url)==0:
    url='http://py4e-data.dr-chuck.net/comments_42.xml'
#
uhandle = urllib.request.urlopen(url)
data = uhandle.read()
tree = ET.fromstring(data)
comlst = tree.findall('comments/comment')
print("size:",len(comlst))
#
sum = 0
for com in comlst:
    val = com.find('count').text
    num = int(val)
    sum += num
print("Sum:",sum)
#
