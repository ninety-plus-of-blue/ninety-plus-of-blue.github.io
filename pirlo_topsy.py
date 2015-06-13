import json
import urllib2

url = 'http://otter.topsy.com/linkposts.json?url=http://futbol.as.com/futbol/2015/06/03/champions/1433294325_459141.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#hdr = { 'User-Agent' : user_agent, 'Content-Type': 'application/json' }
request = urllib2.Request(url)
request.add_header('User-Agent',user_agent)
response = urllib2.urlopen(request)
data = json.load(response)
counter = 0
for tweet in data['response']['list']:
    counter += 1
    print tweet['content']