# encoding: utf-8
"""
@author: chen km
@contact: 760855003@qq.com
@file: clipRaster.py
@time: 2019/5/18 21:23
"""
import arcpy
from arcpy import env
import numpy as np
import arcpy
from arcpy.sa import *
import os
import re

filedir = r'I:\result2\12547'
env.workspace = filedir
files = os.listdir(filedir)
files = [file for file in files if file.endswith('.tif')]
# filedirW = r'I:\result2\12547'
# wrss = list(set([x[-9:-4] for x in files]))

MaskRaster = files[-1]
i = 0
for file in files:
    arcpy.Clip_management(
        file,
        '108.231450881987 18.1458789076859 108.901144926298 19.4777211479215',
        os.path.join(
            filedir,
            'clip_' + file),
        MaskRaster,
        '-1.797693e+308',
        'NONE',
        'NO_MAINTAIN_EXTENT')
    i += 1
    print(u'处理第 %s个，名称是 %s' % (str(i), file))

#  裁剪相应的区域
path = r"I:\result2\test1\ResultsYearShp"
env.workspace = path
rasters = os.listdir(path)
rasters = [x for x in rasters if re.search(r'^\d{4}\.shp$', x) is not None]
inMaskDataAll = os.path.join(path, "fujian_mask.shp")
inMaskDataAll = os.path.join(path, "Mfujian.shp")
for inRaster in rasters[1:]:
    file = os.path.join(path,inRaster)
    fileNew = os.path.join(path, 'Mfujian_' + inRaster)
    arcpy.Clip_analysis(file, inMaskDataAll, fileNew, '#')
    print(inRaster)

path = r"I:\result2\test1\ResultsYearShp"
arcpy.env.workspace = path
rasters = os.listdir(path)
rasters = [x for x in rasters if re.search(r'^fujian_\d{4}\.shp$', x) is not None]
for infc in rasters:
    # 必须进行更新
    arcpy.AddField_management(infc, 'area', 'double')
    arcpy.CalculateField_management(
    infc, "area", "!shape.area@squarekilometers!", "PYTHON_9.3"
    )
