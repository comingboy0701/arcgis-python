# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:30:49 2019

@author: dell
"""
import geopandas
from pandas import DataFrame
import os,re

path = r'I:\result2\spartina\point'

shps = []
i = 0
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if name.endswith('.shp'):
            i = i+1
            file = os.path.join(root, name)
            shps.append(file)
            print('deal number is: %s ,file names: %s\n' % (str(i), file))

points = {} 

for file in shps:
    year= file[-16:-12]
    file_1 = os.path.join(path,file)
    point_1 = [str(x) for x  in geopandas.read_file(file_1)['geometry'] ]
    points_last =  points.keys()    
    for point in point_1:
        yearMark ={'class'+str(x) : 0 for x in range(1986,2019)}
        key = 'class'+str(year)
        if point not in points_last:
            yearMark[key] = 2
            points[point] = yearMark
        else:
            yearMark = points[point]
            yearMark[key] = 2
            points[point] =yearMark


points_rv = DataFrame(points)
points_rv = points_rv.T
xy = [re.sub(r'[(|)]','',x).split() for x in list(points_rv.index)]
points_rv['coord.x'] = [x[1] for x in xy]
points_rv['coord.y'] = [x[2] for x in xy]
points_rv = points_rv.reset_index(drop=True)
points_rv.to_csv('point_wrs.csv',index = False,header = True,sep = ',')
