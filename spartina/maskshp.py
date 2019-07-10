# encoding: utf-8
"""
@author: chen km
@contact: 760855003@qq.com
@file: maskshp.py
@time: 2019/6/12 17:00
"""
#  裁剪相应的区域
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os
import re

wrs = '117044'  #
shpdir = os.path.join(r'I:\result2\spartina\shp', wrs)
maskshp = r'I:\result2\spartina\clip\125045.shp'
i = 0
for root, dirs, files in os.walk(shpdir, topdown=False):
    for name in files:
        if name.endswith('.shp'):
            i += 1
            file = os.path.join(root, name)
            # fileNew = os.path.join(shpdir, '.'.join(
            #     ['shp'+os.path.splitext(file)[0][-12:], 'shp']))
            fileNew = os.path.join(r'I:\result2\spartina\shp\\'+wrs+'_2', '.'.join(
                ['shp' + os.path.splitext(file)[0][-12:], 'shp']))
            arcpy.Clip_analysis(file, maskshp, fileNew, '#')
            print(
                    u'deal number %s，source name is %s, result is %s' %
                    (str(i), file, fileNew))

