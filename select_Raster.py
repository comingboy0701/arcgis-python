# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:48:19 2019

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:43:56 2019

@author: dell
"""

import gdal, ogr, osr, os
import numpy as np

def raster2array(rasterfn):
    raster = gdal.Open(rasterfn)
    band = raster.GetRasterBand(1)
    return band.ReadAsArray()

def getNoDataValue(rasterfn):
    raster = gdal.Open(rasterfn)
    band = raster.GetRasterBand(1)
    return band.GetNoDataValue()

def array2raster(rasterfn,newRasterfn,array):
    raster = gdal.Open(rasterfn)
    geotransform = raster.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]
    cols = raster.RasterXSize
    rows = raster.RasterYSize

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Float32)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromWkt(raster.GetProjectionRef())
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()


filedir = r'I:\result2\Result2'
files = os.listdir(filedir)
files  = [file for file in files if file.endswith('.tif')]
filedirW = r'I:\result2\ResultSP'

i = 0
for file in files:
 
    fileone = os.path.join(filedir,file)
    rasterArray = raster2array(fileone)
    rasterArray[rasterArray != 2] = 'nan'    
    fileNew = os.path.join(filedirW,'sp2_'+file)
    array2raster(fileone,fileNew,rasterArray)
    i +=1
    print('处理第 %s个，名称是 %s' %(str(i),file))

