# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:28:01 2019

@author: dell
"""

import gdal, ogr, osr, os,shutil
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

wrs = '123045'#120043,119043
filedir = os.path.join(r'I:\result2\spartina\tif', wrs)

fileA = ['clip_sp_train200012_12345.tif','clip_sp_train200312_12345.tif',]#'good'

fileBs = ['clip_sp_train200112_12345.tif',
          'clip_sp_train200212_12345.tif',
          ]#bad

for fileB in fileBs:
    file2001 = os.path.join(filedir,fileB)
    
    
    tif2000 = raster2array(os.path.join(filedir,fileA[0]))
    tif2003 = raster2array(os.path.join(filedir,fileA[1]))
    
    tif2001 = raster2array(file2001)
    
    file2001_new = os.path.join(filedir,os.path.splitext(fileB)[0]+'_2.tif')
    raster2001 = np.zeros(tif2000.shape)
    index2001 = ((tif2000+tif2001)==4) +((tif2001+tif2003)==4)==1
    raster2001[index2001] = 2
    array2raster(file2001,file2001_new,raster2001)






