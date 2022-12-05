import urllib.request, urllib.parse, urllib.error
import json
#
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
#
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
#
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
#
    try:
        js = json.loads(data)
    except:
        js = None
#
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
#
    #print(json.dumps(js, indent=4))
#
    id = js['results'][0]['place_id']
    print('Place ID:', id)
