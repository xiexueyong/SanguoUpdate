#! /usr/bin/env python
# -*- coding: utf-8 -*-

#2015-07-28 20:13:20.160636+08:00
import GlobalConfig
from createUpdateZip import *
from createChannelExcel import *
from createUpdateExcel import * 
import shutil 


mergeEveryAssetsSo()

if GlobalConfig.branch == "dataeyeUpdate":
    shutil.copyfile(GlobalConfig.win_projectPath+'/releaseFold/updatefile/core_channel.xlsx',GlobalConfig.win_projectPath+'/releaseFold2/updatefile/core_channel.xlsx')
    shutil.copyfile(GlobalConfig.win_projectPath+'/releaseFold/updatefile/core_update.xlsx',GlobalConfig.win_projectPath+'/releaseFold2/updatefile/core_update.xlsx')
    
createChannelVersionExcel()
createUpdateExcel()