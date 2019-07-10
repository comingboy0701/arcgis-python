# encoding: utf-8
"""
@author: chen km
@contact: 760855003@qq.com
@file: shp2kmz.py
@time: 2019/6/13 14:34
"""
import arcpy
import os

wrs = '120043'
filedir = os.path.join(r'I:\result2\spartina\shp', wrs)
targetdir = os.path.join(r'I:\result2\spartina\kmz', wrs)
files = os.listdir(filedir)
files = [file for file in files if file.endswith('.shp')]

i = 0
for file in files:
    fileNew = os.path.join(targetdir, os.path.splitext(file)[0] + '.kmz')
    arcpy.LayerToKML_conversion(
        file[:-4],
        fileNew,
        '0',
        'NO_COMPOSITE',
        '#')
    i += 1
    print(u'deal number %s，source name is %s, result is %s' % (str(i), file[:-4], fileNew))

