# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:02:40 2019

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:57:10 2019

@author: dell
"""

import geopandas
import os
# shp 进行处理 ,以及合并

wrs = '123045' #120043
filedir = os.path.join(r"I:\result2\spartina\shp",wrs)

i = 0
for root, dirs, files in os.walk(filedir, topdown=False):
    for name in files:
        if name.endswith('.shp'):
            i += 1
            file = os.path.join(root, name)
            fileNew = os.path.join(root, 'shp'+name)
            data = geopandas.read_file(file)
            data2 = data.loc[data['gridcode']==2,:]
            data2.to_file(fileNew)
            print(u'deal number %s，source name is %s, result is %s' % (str(i), file, fileNew))


