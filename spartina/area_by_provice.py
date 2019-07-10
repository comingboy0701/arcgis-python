# encoding: utf-8 
""" 
@author: chen km 
@contact: 760855003@qq.com 
@file: area_by_provice.py 
@time: 2019/7/7 10:48 
"""
import arcpy
from arcpy.sa import *
import pandas as pd
import re,os

file_dir = r"I:\result2\spartina\mergeshp" # 改变相应的目录就好
arcpy.env.workspace = file_dir
region = r'I:\result2\spartina\clip\provice.shp' #三个不同区域的 shp 图层
i = 0
for root, dirs, files in os.walk(file_dir, topdown=False):
    for name in files:
        if name.endswith('.shp') and name.startswith('u') and str(1986) not in name:
            i = i+1
            infc = os.path.join(root, name)
            inFeatures = [infc, region]
            intersectOutput = os.path.join(root, 'Pro_'+name)
            arcpy.Intersect_analysis(inFeatures, intersectOutput) # 把 shp 按 不同区域分区
            print('deal number is: %s ,Intersect_analysis: %s\n' % (str(i), intersectOutput))

            arcpy.AddField_management(intersectOutput, 'area', "DOUBLE") # 增加 area 字段
            print('deal number is: %s ,AddField_management: %s\n' % (str(i), intersectOutput))

            arcpy.CalculateField_management(
                intersectOutput, "area", "!shape.area@squaremeters!", "PYTHON_9.3"  # 计算几何面积
            )
            print('deal number is: %s ,CalculateField_management: %s\n' % (str(i), intersectOutput))
