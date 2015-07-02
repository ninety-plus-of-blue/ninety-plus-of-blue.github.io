import tweepy
import csv
import cPickle as pickle

#csv writers
f = open('tweet_coordinates.csv','w') 
csv_writer = csv.writer(f)
csv_writer.writerow(['coordinates','blue %','red %','blue count', 'red count'])
'''
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'BvkxtoSU9qNK4s3nncattaRZM'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'uZLIQ6C0PmMGwLHuO5mIhlFUMKeoTUHBmsfnqLKEviKwazsKVw'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '615528592-FuZIIFycOEmyNaEUtSMXpJ5iyPZSEqK5Oz4I7GoN'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Ospy8ZPsgNPkUWhbuG8DsjNVfLwZZXYG1RjKSYD7Ob9Eh'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,timeout=1200)
with open('latest_id.txt','r') as f:
    last_id = int(f.readline())
'''
shapes_dict = pickle.load(open('shapes_dict.p','rb'))
location_dict = {}
geo_dict = {}
coordinates_dict = {}
place_dict = {}
'''
try:
    for x,n in enumerate(tweepy.Cursor(api.search,q='#winrbny',since_id=613628562382430208,lang="en").items()):
        if x > 100000:
            break
        else:
        #print x,n.text.encode('utf-8')
            tweet_count_blue = x
            print "red",tweet_count_blue
            if n.place != None:
                #print x, n.text.encode('utf-8'), n.place.bounding_box.coordinates
                place_dict[x] = [n.text.encode('utf-8'),n.place.bounding_box.coordinates[0]]
                print place_dict[x]
                text = n.text
                thing = place_dict[x]
                point1 = "Polygon((%s %s, %s %s, %s %s, %s %s, %s %s))" % (thing[1][0][0],thing[1][0][1],thing[1][1][0],thing[1][1][1],thing[1][2][0],thing[1][2][1],thing[1][3][0],thing[1][3][1],thing[1][0][0],thing[1][0][1])
                if point1 in shapes_dict.keys():
                    shapes_dict[point1][1] += 1
                else:
                    shapes_dict[point1] = [0,1]
            try:
                location_dict[x] = [n.author._json['location']]
            except:
                pass

            pickle.dump(shapes_dict,open('shapes_dict.p','wb'))
            pickle.dump(location_dict,open('location_dict_rbny.p','wb'))
            with open('latest_id_rbny.txt','w') as f:
                f.write(str(n.id))

except IOError, ex:
    print 'I just caught the exception: %s' % ex
    time.sleep(100)
'''
'''
try:
    for x,n in enumerate(tweepy.Cursor(api.search,q='#winrbny',
                        since_id="2015-06-24",
                        lang="en").items()):
        if x > 100000:
            break
        else:
        #print x,n.text.encode('utf-8')
            tweet_count_red = x
            print "red",tweet_count_red
            if n.place != None:
                #print x, n.text.encode('utf-8'), n.place.bounding_box.coordinates
                place_dict[x] = [n.text.encode('utf-8'),n.place.bounding_box.coordinates[0]]
                print place_dict[x]
                text = n.text
                thing = place_dict[x]
                point1 = "Polygon((%s %s, %s %s, %s %s, %s %s, %s %s))" % (thing[1][0][0],thing[1][0][1],thing[1][1][0],thing[1][1][1],thing[1][2][0],thing[1][2][1],thing[1][3][0],thing[1][3][1],thing[1][0][0],thing[1][0][1])
                if point1 in shapes_dict.keys():
                    shapes_dict[point1][1] += 1
                else:
                    shapes_dict[point1] = [0,1]
            try:
                location_dict[x] = [n.author._json['location']]
            except:
                pass
except IOError, ex:
    print 'I just caught the exception: %s' % ex
    time.sleep(10)
'''
#print location_dict.items()

#print place_dict.items()
'''
with open('kartograph-test/world.json','a') as f:
    for thing in place_dict.items():
        text = thing[1][0]
        point1 = "Polygon((%s %s, %s %s, %s %s, %s %s, %s %s))" % (thing[1][1][0][0],thing[1][1][0][1],thing[1][1][1][0],thing[1][1][1][1],thing[1][1][2][0],thing[1][1][2][1],thing[1][1][3][0],thing[1][1][3][1],thing[1][1][0][0],thing[1][1][0][1])
        if point1 in shapes_dict.keys():
            shapes_dict[point1] += 1
        else:
            shapes_dict[point1] = 1
'''

for key in shapes_dict.keys():
    blue = shapes_dict[key][0]/float(shapes_dict[key][0]+shapes_dict[key][1])
    red = shapes_dict[key][1]/float(shapes_dict[key][0]+shapes_dict[key][1])
    csv_writer.writerow([key,blue,red,shapes_dict[key][0],shapes_dict[key][1]])

        #f.write('\n"%s": {\n"%s",\n"lon0": %s,\n"lat0": %s\n}' %
                #(thing[0],text,longitude,latitude))
print shapes_dict
#for place in place_dict['coordinates']:
    #lat0 = place[0][0][0]
    #lon0 = place[0][0][1]

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

f.close()
