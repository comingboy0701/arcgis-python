# encoding: utf-8 
""" 
@author: chen km 
@contact: 760855003@qq.com 
@file: shp2merge.py 
@time: 2019/7/2 16:22 
"""
# 由 把每年的小shp 文件合并成一个大shp
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os, re

file_dir = r'I:\result2\spartina\shp'
file_dir_2 = os.listdir(file_dir)

shps = []
i = 0
for root, dirs, files in os.walk(file_dir, topdown=False):
    for name in files:
        if name.endswith('.shp') and name.startswith('shp'):
            i = i+1
            file = os.path.join(root, name)
            shps.append(file)
            print('deal number is: %s ,file names: %s\n' % (str(i), file))



results_dir = r'I:\result2\spartina\mergeshp'
i = 18
for year in range(2004,2019):
    year_shs = [shp for shp in shps if 'shp'+str(year) in shp ]
    shp2merge = os.path.join(results_dir,'m'+str(year)+'.shp')
    # 合并shp
    arcpy.Union_analysis(year_shs,  shp2merge, 'ALL', '#', 'GAPS')  # 'test1 #;test2 #'
    # 消除公共边
    shp2comm = os.path.join(results_dir, 'u'+str(year)+'.shp')
    arcpy.Dissolve_management(os.path.join(file_dir, shp2merge), os.path.join(file_dir, shp2comm), '#', '#', 'SINGLE_PART', 'UNSPLIT_LINES')
    i += 1
    print('deal number is: %s ,file names: %s\n' % (str(i), str(shp2comm)))


