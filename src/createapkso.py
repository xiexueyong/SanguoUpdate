#! /usr/bin/env python
# -*- coding: utf-8 -*-
from limebuildSerially import *
from GlobalConfig import * 
import os
import shutil

def removeFileInFirstDir(targetDir,exceptFiles=[]): 
    for file in os.listdir(targetDir):
        ignore = False 
        for f in exceptFiles:
            if f==file:
                ignore = True
        if ignore:
            continue
        
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(targetFile): 
            os.remove(targetFile)
        else:
            shutil.rmtree(targetFile)
            
#删除上一次打包留下的老文件。
#removeFileInFirstDir(win_diffAssetsPath,['updatefile'])
#removeFileInFirstDir(win_updateFilePath,['core_channel.xlsx','core_update.xlsx'])
#处理各个渠道的更新包
for channel in channels:
    createApkSoFlash(channelIndex[channel],channel)
    
