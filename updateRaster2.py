# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:53:51 2019

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

i = 0
dirS = r'I:\result2\ResultSP'
dirs = os.listdir(dirS)
for dirone in dirs:
    dirone = dirs[5]
    
    dirsS = os.path.join(dirS,dirone)
    files = os.listdir(dirsS)
    files  = [file for file in files if file.endswith('.tif') and file.startswith('test')]   
    wrsFile = files[::-1]
    for index,file in enumerate(wrsFile):
#        index,file = 1,wrsFile[1]
        filebefore = os.path.join(dirsS,file)
        rasterbefore = raster2array(filebefore)
        rasterbefore[rasterbefore!=2] = 'nan'
        
        if index==0:
            array2raster(filebefore,filebefore,rasterbefore)
            i+=1
            print('处理第 %s个，名称是 %s' %(str(i),file))
        else: 
            
            raster3 = np.zeros(rasterbefore.shape)
            for fileNext in wrsFile[max(index-5,0):index]:
                
                filenext = os.path.join(dirsS,fileNext)
                rasterNext = raster2array(filenext)
                rasterNext[rasterNext!=2]=0
                raster3 = raster3+rasterNext
            
            rasterbefore[raster3 < min(8,index*2)] = 'nan'            
            array2raster(filebefore,filebefore,rasterbefore)
            i+=1
            print('处理第 %s个，名称是 %s' %(str(i),file))




