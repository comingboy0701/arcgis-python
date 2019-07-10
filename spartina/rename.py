# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:53:23 2019

@author: dell
"""


import os
path = r'I:\result2\spartina\tif_result'
i = 0
# 修改file 的名字
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        file = os.path.join(root, name)
        fileNew = os.path.join(root, name[-24:])
        os.rename(file, fileNew)  # 修改文件名字
        i += 1
    print(u'dealnumber %s:file is: %s;fileNew is: %s' %
          (str(i), name, name[-24:]))

# 删除file
path = r'I:\result2\spartina\tif_result'
j = 0
i = 0
for root, dirs, files in os.walk(path, topdown=False):
    j = j+1
    for name in files:
        name = str(name).strip()
        if  not (name.startswith('Nodata') and name.endswith('.tif')):
            file = os.path.join(root, name)
            os.remove(file)  # 删除文件
            i += 1
            print(u'dealnumber %s:file is: %s; %s'  %(str(j), str(i),str(name)))
