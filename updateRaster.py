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


file_2000 = 'I:\result2\spartina\120043\sp_train200012_12043.tif'
file_2003 = 'I:\result2\spartina\120043\sp_train200012_12043.tif'

filedirS = r'I:\result2\Result2'
files = os.listdir(filedirS)
files  = [file for file in files if file.endswith('.tif')]

wrss = list(set([x[-9:-4] for x in files]))

filedir = r'I:\result2'
i = 0
for wrs in wrss:
    
    wrs = wrss[1] #27,0,1
    wrsFiles = [x for x in files if wrs in x]
    
    try:
        os.mkdir(os.path.join(filedir,str(wrs)))
    except:
        pass
    filedirT = os.path.join(filedir,str(wrs))
    wrscp = wrsFiles[::1]
    for file in wrscp:
        shutil.copy(os.path.join(filedirS,file),filedirT)
        print('复制文件 %s' %(file))
    
    wrsFile = wrsFiles[::-1]
    
    for index,file in enumerate(wrsFile):
#        index,file = 0,wrsFile[0]
        filebefore = os.path.join(filedirT,file)
        rasterbefore = raster2array(filebefore)
        rasterbefore[rasterbefore!=2] = 'nan'
        
        if index==0:
            array2raster(filebefore,filebefore,rasterbefore)
            i+=1
            print('处理第 %s个，名称是 %s' %(str(i),file))
        else: 
            
            raster3 = np.zeros(rasterbefore.shape)
            for fileNext in wrsFile[max(index-3,0):index]:
                
                filenext = os.path.join(filedirT,fileNext)
                rasterNext = raster2array(filenext)
                raster3[rasterNext == 2] = 2
            
            rasterbefore[raster3 !=2 ] ='nan'
            
            array2raster(filebefore,filebefore,rasterbefore)
            i+=1
            print('处理第 %s个，名称是 %s' %(str(i),file))




