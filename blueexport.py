# coding: utf-8
import cPickle as pickle
import csv
shapes = pickle.load(open('shapes_dict.p','r'))
totes_blue = 0
writer = csv.writer(open('blue_boxes.csv','w'))
writer.writerow(['coordinates','bluecount','bluepercent'])

for shape in shapes.items():
    totes_blue += shape[1][0]
    
for shape in shapes.items():
    a = (int(shape[1][0])/float(totes_blue))*100
    writer.writerow([shape[0],int(shape[1][0])*.01,"%"+str(round(a,2))])
    print [shape[0],int(shape[1][0])*.01,"%"+str(round(a,2))]
    
