# -*- coding: utf-8 -*-
import arcpy
from arcpy import env
import numpy as np
import arcpy
import os, re

# 由 double 类型转换成 int 类型
Dir = r"I:\result2\ResultSP"
dirs = os.listdir(Dir)
i = 0
for root, dirs, files in  os.walk(Dir, topdown=False):
    for name in files:
        file = os.path.join(root, name)
        fileNew = os.path.join(root, 'int_'+name)
        express = 'Int("%s")' % file
        result = arcpy.gp.RasterCalculator_sa(express, fileNew)
        i += 1
        print(u'deal double to Int number %s，name is %s' % (str(i), file))

# 由栅格数据转换成 shp 矢量文件
filewr = r"I:\result2\ResultsShp"
i = 0
erro = []
for root, dirs, files in os.walk(Dir, topdown=False):
    for name in files:
        if name.endswith('.tif') and name.startswith('int_'):
            try:
                i += 1
                file = os.path.join(root, name)
                fileNew = os.path.join(filewr, '.'.join([os.path.splitext(file)[0][-16:], 'shp']))
                arcpy.RasterToPolygon_conversion(file, fileNew, 'NO_SIMPLIFY', 'Value')
                print(u'deal number %s，source name is %s, result is %s' % (str(i), file, fileNew))
            except:
                print('erro number is: %s ,file names: %s\n' % (str(i), file))
                with open('erroshp.txt', 'ab+') as f:
                    f.write('erro number is: %s ,file names: %s\n' % (str(i), file))
                pass


# 由 把每年的小shp 文件合并成一个大shp
env.workspace = filewr
fileDiry = r'I:\result2\ResultsYearShp'
i = 0
for year in range(1986, 2019):
    shp = 'test%s*.shp' % str(year)
    shps = arcpy.ListFeatureClasses(shp, 'Polygon')
    shps = ' #;'.join(shps)
    file = 'U'+str(year) + '.shp'
    # 合并shp
    arcpy.Union_analysis(shps, os.path.join(fileDiry, file), 'ALL', '#', 'GAPS')  # 'test1 #;test2 #'
    # 消除公共边
    fileR = os.path.join(fileDiry, file)
    arcpy.Dissolve_management(fileR, os.path.join(fileDiry, str(year)+'.shp'), '#', '#', 'SINGLE_PART', 'UNSPLIT_LINES')
    i += 1
    print(u'deal number %s，year is %s ' % (str(i), str(year)))