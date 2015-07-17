import tweepy
import csv
import geocoder

#csv writers
f = open('user_locations.csv','w') 
csv_writer = csv.writer(f)
csv_writer.writerow(['name','x','y','count'])

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
    if x > 500:
        break
    else:
    #print x,n.text.encode('utf-8')
        tweet_count = x
        print tweet_count
        ''' 
        if n.place != None:
            #print x, n.text.encode('utf-8'), n.place.bounding_box.coordinates
            place_dict[x] = [n.text.encode('utf-8'),n.place.bounding_box.coordinates[0]]
            print place_dict[x]'''
        try:
            location_dict[x] = [n.author._json['location']]
        except:
            pass

for location in location_dict.values():
    print location
    if location[0] != u'':
        new_loc = location[0].lower()
        g=geocoder.google(new_loc)
        if g.latlng != []:
            if new_loc in coordinates_dict.keys():
                coordinates_dict[new_loc][3] += 1
            else:
                coordinates_dict[new_loc] = [new_loc,g.latlng[0],g.latlng[1],1]

for thing in coordinates_dict.values():
    csv_writer.writerow(thing)
    #f.write('\n"%s": {\n"%s",\n"lon0": %s,\n"lat0": %s\n}' % (thing[0],text,longitude,latitude))

#for place in place_dict['coordinates']:
    #lat0 = place[0][0][0]
    #lon0 = place[0][0][1]

'''    if not location_dict[n.location]:
        location_dict[n.location] = 1
    else
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

f.close()
