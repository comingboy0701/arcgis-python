# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:16:52 2019

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
    
    
path_dirs = r'I:\result2\spartina\tif_result'
wrs_all = ['120043']#os.listdir(path_dirs)
i = 0 
for wrs in wrs_all:
    path = os.path.join(r'I:\result2\spartina\tif_result', wrs)
    shps =  [ i for i in os.listdir(path) if i.endswith('.tif') and (i.startswith('sp_'))]
    for index,shp in enumerate(shps):
        index_s= max(index -3,0)
        index_e= min(index + 3,len(shps))
        file_now = os.path.join(path,shp)
        file_now_new = os.path.join(path,'con5_'+shp)
        tif_now = raster2array(file_now)
        raster_now = np.zeros(tif_now.shape)
        for shp_conti in shps[index_s:(index_e+1)]:
            
            file_1 = os.path.join(path,shp_conti)
            tif_1 = raster2array(file_1)
            tif_now = tif_now+tif_1
        
        index4 = (np.int16(tif_now<= 2*5)+np.int16(2*5 <= tif_now))==2
        
        raster_now[index4] = 2
        
        np.max(raster_now)

        array2raster(file_now,file_now_new,raster_now)
        i += 1
        print(u'dealnumber %s:file is: %s' % (str(i), file_now_new))

    
        

