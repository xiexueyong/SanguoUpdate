#! /usr/bin/env python
# -*- coding: utf-8 -*-
from limebuildSerially import *
from GlobalConfig import * 

#处理各个渠道的更新包
for channel in channels:
    createApkSoFlash(channelIndex[channel],channel)
    
