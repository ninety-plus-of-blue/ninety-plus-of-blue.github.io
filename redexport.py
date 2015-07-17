# coding: utf-8
import cPickle as pickle
import csv
shapes = pickle.load(open('shapes_dict.p','r'))
totes_red = 0
writer = csv.writer(open('red_boxes.csv','w'))
writer.writerow(['coordinates','redcount','redpercent'])

for shape in shapes.items():
    totes_red += shape[1][1]
    
for shape in shapes.items():
    a = (int(shape[1][1])/float(totes_red))*100
    writer.writerow([shape[0],int(shape[1][1])*.01,"%"+str(round(a,2))])
    print [shape[0],int(shape[1][1])*.01,"%"+str((int(shape[1][1])/float(totes_red))*100)]
    
