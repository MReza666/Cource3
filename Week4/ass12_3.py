import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#
url=input('insert URL: ')
if len(url)==0:
    url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
repeats=int(input('insert No of repeats:'))
position=int(input('insert link position:'))
#
for rep in range(repeats+1):
    print('Retrieving:', url)
    uhandle = urllib.request.urlopen(url)
    html = uhandle.read()
    soup = BeautifulSoup(html, 'html.parser')
#
    tags = soup('a')
    link=tags[position-1].get('href', None)
    url=link
#
