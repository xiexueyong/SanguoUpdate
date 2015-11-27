#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import channelSwitch
import shutil
import time
from GlobalConfig import * 

timestr = time.strftime("%Y-%m-%d-%H-%M")

def createApkSoFlash(channelIndex,channelSuffix):
    channelSwitch.switch(channelIndex)
    os.chdir(win_projectPath)
    changeAndroidFoldName(debug)
    if debug:
        os.system('lime build android -debug --no-traces')
    else:
        os.system('lime build android --no-traces')
    shutil.copyfile(win_apkPath,win_targetApkPath+"/PtSanguo-%s-%s.apk"%(channelSuffix,timestr))
    shutil.copyfile(win_soPath, win_targetSoPath+"/libApplicationMain-%s.so"%(channelSuffix))
    #葡萄版本，打一个flash
    if channelSuffix=='putaogame' or channelSuffix=='dangbei' or channelSuffix=='lovegame':
        #os.system('lime build flash')
        #shutil.copyfile(win_swfPath, win_targetApkPath+"/PtSanguo-%s-%s.swf"%(channelSuffix,timestr))
        print 'create flash'
    
def changeAndroidFoldName(debug):
    debugPath = win_projectPath+"/export/android_debug"
    releasePath = win_projectPath+"/export/android_release"
    currAndroidPath = win_projectPath+"/export/android"
    
    if debug:
        doDebugMode(releasePath,debugPath,currAndroidPath)
    else:
        doReleaseMode(releasePath,debugPath,currAndroidPath)
       
def doDebugMode(releasePath,debugPath,currAndroidPath):
    if os.path.exists(debugPath):      
       os.rename(currAndroidPath,releasePath)
       os.rename(debugPath,currAndroidPath)       
def doReleaseMode(releasePath,debugPath,currAndroidPath):        
    if os.path.exists(releasePath):
       os.rename(currAndroidPath,debugPath)
       os.rename(releasePath,currAndroidPath)
    