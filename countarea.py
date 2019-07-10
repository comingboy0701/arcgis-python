# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:29:22 2019

@author: dell
"""

import os, re
import geopandas
import pandas as pd
import numpy as np 
import matplotlib.pylab as plt
import matplotlib
import brewer2mpl


plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

font = {'family':'Microsoft YaHei', 'weight':'bold', 'size':12}
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
matplotlib.rc('font', **font)


bmap = brewer2mpl.get_map('Dark2', 'qualitative', 8)
color = bmap.mpl_colors

path = r"I:\result2\test1\ResultsYearShp"
rasters = os.listdir(path)
rasters = [x for x in rasters if re.search(r'^fujian_\d{4}\.shp$', x) is not None]
data = pd.DataFrame(columns = ['file','area'])
dicts = {'area':0,'file':0}
for raster in rasters:
    file = os.path.join(path,raster) 
    are = geopandas.read_file(file)
    dicts['file'] = np.int(re.search(r'\d{4}',raster).group(0))
    dicts['area'] = sum(are['area'])
    data = data.append(dicts, ignore_index=True)
    
kw2 = dict(linewidth = 2,markerfacecolor= 'red',markeredgecolor='red',markersize = 6,)
fig = plt.figure(figsize=(16, 10))
plt.plot(data['file'],data['area'],'o-' ,color = color[0], label = '面积',**kw2)
plt.xticks(range(1986,2020,2))
plt.ylabel('面积(km$^2$)',fontsize = 16)
plt.legend()
plt.grid()
plt.savefig("福建米草面积",format='png', bbox_inches='tight', transparent=True,dpi=1200)
plt.show()