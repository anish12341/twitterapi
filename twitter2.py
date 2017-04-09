import urllib
import twurl
import json
TWITTER_URL='https://api.twitter.com/1.1/friends/list.json'
while True:
    print ''
    acct=raw_input('Enter Twitter Account:')
    if(len(acct)<1):break
    url=twurl.augment(TWITTER_URL,{'screen_name':acct,'count':'10'})
    print 'Retrieving',url
    connection=urllib.urlopen(url)
    data=connection.read()
    headers=connection.info().dict
    print 'Remaining',headers['x-rate-limit-remaining']
    js=json.loads(data)
    for u in js['users']:
	   print u['screen_name']
	   s=u['status']['text']
	   print '   ',s[:20]