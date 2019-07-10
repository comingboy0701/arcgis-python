# encoding: utf-8
"""
@author: chen km
@contact: 760855003@qq.com
@file: raster2shp.py
@time: 2019/6/10 13:15
"""
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os
import re

wrs = '123045'  # 120043
filedir = os.path.join(r'I:\result2\spartina\tif', wrs)
shpdir = os.path.join(r'I:\result2\spartina\shp', wrs)
i = 0
for root, dirs, files in os.walk(filedir, topdown=False):
    for name in files:
        if name.endswith('.tif') and name.startswith('clip_'):
            i += 1
            file = os.path.join(root, name)
            fileNew = os.path.join(shpdir, '.'.join(
                [os.path.splitext(file)[0][-12:], 'shp']))
            arcpy.RasterToPolygon_conversion(
                file, fileNew, 'NO_SIMPLIFY', 'Value')
            print(
                u'deal number %s，source name is %s, result is %s' %
                (str(i), file, fileNew))
