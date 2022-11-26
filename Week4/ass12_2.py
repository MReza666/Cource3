import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
#
url=input('insert URL: ')
if len(url)==0:
    url='http://py4e-data.dr-chuck.net/comments_42.html'
#print(url)
uhandle = urllib.request.urlopen(url)
html = uhandle.read()
soup = BeautifulSoup(html, 'html.parser')
#
tags = soup('span')
sum=0
for tag in tags:
    # Look at the parts of a tag
    sum+= int(tag.contents[0])
#
print('Count:',len(tags))
print('Total sum:',sum)
