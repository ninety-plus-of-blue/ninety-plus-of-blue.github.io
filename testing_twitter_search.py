import tweepy
import csv

#csv writers
#f = open('tweet_coordinates.csv','w') 
#csv_writer = csv.writer(f)
#csv_writer.writerow(['id','tweet','coordinates'])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'BvkxtoSU9qNK4s3nncattaRZM'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'uZLIQ6C0PmMGwLHuO5mIhlFUMKeoTUHBmsfnqLKEviKwazsKVw'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '615528592-FuZIIFycOEmyNaEUtSMXpJ5iyPZSEqK5Oz4I7GoN'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Ospy8ZPsgNPkUWhbuG8DsjNVfLwZZXYG1RjKSYD7Ob9Eh'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

location_dict = {}
geo_dict = {}
coordinates_dict = {}
place_dict = {}

for x,n in enumerate(tweepy.Cursor(api.search,q='#winnycfc',
                    since="2015-06-24",
                    lang="en").items()):
    if x > 10:
        break
    else:
        '''
    #print x,n.text.encode('utf-8')
        tweet_count = x
        #print tweet_count
        if n.place != None:
            #print x, n.text.encode('utf-8'), n.place.bounding_box.coordinates
            place_dict[x] = [n.text.encode('utf-8'),n.place.bounding_box.coordinates[0]]
            #print "place",place_dict[x]
        if n.geo != None:
            geo_dict[x] = [n.geo]
            print "geo",geo_dict[x]
        '''
        print n.author._json['location']

#print place_dict.items()
     
'''
with open('kartograph-test/world.json','a') as f:
    for thing in place_dict.items():
        text = thing[1][0]
        point1 = "Polygon((%s %s, %s %s, %s %s, %s %s, %s %s))" % (thing[1][1][0][0],thing[1][1][0][1],thing[1][1][1][0],thing[1][1][1][1],thing[1][1][2][0],thing[1][1][2][1],thing[1][1][3][0],thing[1][1][3][1],thing[1][1][0][0],thing[1][1][0][1])
        csv_writer.writerow([thing[0],text,point1])
        #f.write('\n"%s": {\n"%s",\n"lon0": %s,\n"lat0": %s\n}' %
                #(thing[0],text,longitude,latitude))

#for place in place_dict['coordinates']:
    #lat0 = place[0][0][0]
    #lon0 = place[0][0][1]
'''
'''    if not location_dict[n.location]:
        location_dict[n.location] = 1
    else:
        location_dict[n.location] += 1
    if not geo_dict[n.geo]:
        geo_dict[n.geo] = 1
    else:
        geo_dict[n.geo] += 1
    if not coordinates_dict[n.coordinates]:
        coordinates_dict[n.coordinates] = 1
    else:
        coordinates_dict[n.coordinates] += 1


    with open("winnycfc.txt","a") as myfile:
        myfile.write(str(location_dict.items()))
        myfile.write(str(geo_dict.items()))
        myfile.write(str(coordinates_dict.items()))
    #if not n.text.startswith('RT'):
        #print n.id,n.text
'''

#f.close()
