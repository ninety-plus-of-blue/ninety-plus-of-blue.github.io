import tweepy


#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'BvkxtoSU9qNK4s3nncattaRZM'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'uZLIQ6C0PmMGwLHuO5mIhlFUMKeoTUHBmsfnqLKEviKwazsKVw'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '615528592-FuZIIFycOEmyNaEUtSMXpJ5iyPZSEqK5Oz4I7GoN'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Ospy8ZPsgNPkUWhbuG8DsjNVfLwZZXYG1RjKSYD7Ob9Eh'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

for x,n in enumerate(tweepy.Cursor(api.search,q='pirlo tribeca',
					since="2015-06-11",
					lang="en").items()):
	print x,n.text.encode('utf-8')
	pirlo_count = x
	with open("Pirlo_results.txt","a") as myfile:
		myfile.write(n.text.encode('utf-8')+'\n')
	#if not n.text.startswith('RT'):
		#print n.id,n.text

