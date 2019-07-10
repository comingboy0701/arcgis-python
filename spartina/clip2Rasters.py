# encoding: utf-8
"""
@author: chen km
@contact: 760855003@qq.com
@file: clip2Rasters.py
@time: 2019/6/24 11:03
"""


#  裁剪相应的区域
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os
import re

wrs = '123045'  #
rasters_dir = os.path.join(r'I:\result2\spartina\tif', wrs)
maskshp = r'I:\result2\spartina\clip\shp_clip.shp'
i = 0
for root, dirs, files in os.walk(rasters_dir, topdown=False):
    for name in files:
        if name.endswith('.tif'):
            i += 1
            file = os.path.join(root, name)
            # fileNew = os.path.join(shpdir, '.'.join(
            #     ['shp'+os.path.splitext(file)[0][-12:], 'shp']))
            fileNew = os.path.join(r'I:\result2\spartina\tif\\' + wrs, ''.join(
                ['clip_' + name]))
            # arcpy.Clip_analysis(file, maskshp, fileNew, '#')
            ractByMask = arcpy.sa.ExtractByMask(file, maskshp)  # 裁剪的工具
            ractByMask.save(fileNew)

            print(
                    u'deal number %s，source name is %s, result is %s' %
                    (str(i), file, fileNew))

