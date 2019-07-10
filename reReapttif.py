# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:13:35 2019

@author: dell
"""
import os
import re
dirFile = r'I:\result2\12547'
files = os.listdir(dirFile)
for file in files:
    if not file.endswith('.tif'):
        os.remove(os.path.join(dirFile,file))
        
        
#fileR = [i for i in files if any(True if j in i else False for j in ['(','_1.tif'])]


for file in fileR:
    filev = os.path.join(dirFile,file)
    print(filev)
    os.remove(filev)

    


for file in fileR:
    filev = file.replace(r'(1)','')
    filev = os.path.join(dirFile,filev)
    os.remove(filev)
    os.rename(os.path.join(dirFile,file),filev)
    
