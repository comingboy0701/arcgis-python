# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:22:38 2019

@author: dell
"""

import geopandas
from pandas import DataFrame
import pandas as pd
import os,re
import matplotlib.pyplot as plt
import numpy as np
import brewer2mpl


plt.rcParams["font.sans-serif"] = "Microsoft YaHei"
plt.rcParams["axes.unicode_minus"] = False

bmap = brewer2mpl.get_map('Set1', 'qualitative', 8)

color = bmap.mpl_colors

path = r'I:\result2\spartina\mergeshp'

files = [i for i in os.listdir(path) if i.startswith('Pro_') and i.endswith('.shp')]


year_area = DataFrame()
for shp in files:
    
    shp = os.path.join(path,shp)
    print(shp)
    shp_are = geopandas.read_file(shp) 
    
    shp_are = shp_are.loc[shp_are['area']>2000 ,:] 
    
    year = re.findall(r'\.*?(\d{4})\.shp',shp)[0]
    
    year_area[year]= DataFrame(shp_are['area'].groupby([shp_are['provice']]).sum()).stack()



data = year_area.T
data.columns = data.columns.droplevel(1)
data = data/10**6

data.to_csv('area.csv',index =True,float_format='%.2f')

ax = data.plot(
kind="line",
linewidth=2,
fontsize=14,
figsize=(8, 6),
color=color,
)

ax.set_title("面积变化", fontsize=14)
ax.set_xlabel("年份(年)", fontsize=14)
ax.set_ylabel("km^2", fontsize=14)
ax.legend(fontsize=14)
