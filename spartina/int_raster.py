# encoding: utf-8
"""
@author: chen km
@contact: 760855003@qq.com
@file: int_raster.py
@time: 2019/6/12 10:31
"""
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os
import re

wrs = '123045'  #
filedir = os.path.join(r'I:\result2\spartina\tif', wrs)
files = [i for i in os.listdir(filedir) if i.endswith('_2.tif')]
# maskshp = r'I:\result2\spartina\clip\125045.shp'
for file in files:
    # 转成int
    file_int = os.path.join(filedir, file)
    file_new = os.path.join(filedir, os.path.splitext(file)[0][:-2] + '_3.tif')
    express = 'Int("%s")' % file_int
    result = arcpy.gp.RasterCalculator_sa(express, file_new)
    print(u'raster2int deal double to file is %s' % result)

    # 转成shp
    shpdir = os.path.join(r'I:\result2\spartina\shp', wrs)
    fileshp = os.path.join(shpdir, '.'.join(
        [os.path.splitext(file)[0][-14:], 'shp']))

    arcpy.RasterToPolygon_conversion(file_new, fileshp, 'NO_SIMPLIFY', 'Value')
    print(u'raster2shp deal double to file is %s' % fileshp)
    # 裁剪shp
    # file_clip = os.path.join(shpdir, 'clip_'+'.'.join(
    #     [os.path.splitext(file)[0][-14:], 'shp']))
    # arcpy.Clip_analysis(fileshp, maskshp, file_clip, '#')
    # print(u'clip2shp result is %s' %  file_clip)



# shp 进行处理 ,以及合并
import geopandas
import os
import re

wrs = '123045'  #
shpdir = os.path.join(r'I:\result2\spartina\shp', wrs)
files = [i for i in os.listdir(shpdir) if i.endswith('_2.shp')]

for file in files:
    fileshp = os.path.join(shpdir,file)
    fileNew = os.path.join(shpdir, '.'.join(
        ['shp' + os.path.splitext(file)[0][-14:], 'shp']))
    data = geopandas.read_file(fileshp)
    data2 = data.loc[data['gridcode'] == 2, :]
    data2.to_file(fileNew)
    print(u'result is %s' % fileNew)



