# encoding: utf-8 
""" 
@author: chen km 
@contact: 760855003@qq.com 
@file: raster2int.py 
@time: 2019/7/7 19:24 
"""
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os
import re


import os
path=r'I:\result2\spartina\tif_result'
i = 0
point_path = r'I:\result2\spartina\point'
for root, dirs, files in  os.walk(path, topdown=False):
    for name in files:
        if  name.endswith('.tif') and name.startswith('intcon5_sp') :
            try:
                i += 1
                file_int = os.path.join(root, name)
                # file_new = os.path.join(root, 'int'+name)
                file_new = os.path.join(root, 'Nodata_' + name[-16:])
                # express = 'Int("%s")' % file_int
                # arcpy.gp.RasterCalculator_sa(express, file_new)
                # print(u'deal number is: %s; raster2int deal double to file is %s' % (str(i),file_new))
                # 转成point
                express = "SetNull('%s'==0,'%s')" % (file_int,file_int)
                arcpy.gp.RasterCalculator_sa(express,file_new)
                print(u'deal number is: %s; raster2int deal double to file is %s' % (str(i), file_new))
                wrs = re.findall(r'.*?(\d{6})',root)[0]
                shpdir = os.path.join(point_path, wrs)
                fileshp = os.path.join(shpdir, '.'.join([os.path.splitext(name)[0][-12:], 'shp']))
                arcpy.RasterToPoint_conversion(file_new, fileshp, 'Value')
                print(u'deal number is: %s; raster2point deal double to file is %s' % (str(i),fileshp))
                print('*' * 50)
            except:
                pass