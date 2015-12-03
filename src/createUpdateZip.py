#! /usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import os
import shutil

from GlobalConfig import * 

#递归压缩函数
def compressFunction(fold,zipF):
    if os.path.isdir(fold):  
        for d in os.listdir(fold):
            subpath = fold+os.sep+d
            zipF.write(subpath)
            if os.path.isdir(subpath):
                compressFunction(subpath,zipF)
#压缩一个文件夹
def compressFold(fold,zipName):
    com_z =zipfile.ZipFile(zipName, 'w',zipfile.ZIP_DEFLATED) 
    compressFunction(fold,com_z)
    com_z.close()

def deleteFile(path):
    if os.path.exists(path):
        print "delete:"+path
        os.remove(path)
#针对一个差异文件（2个tag之间），创造出各个渠道的更新文件
def mergeOneAssetsSo(oldTag='v1.4.0b',targetTag='v1.4.2b'):
    #解压缩
    zipName = 'update-%s-%s-noso.zip'%(oldTag,targetTag)
    zipPath = win_diffAssetsPath+'/'+zipName
    _extractFold = win_diffAssetsPath+'/%s-%s'%(oldTag,targetTag) 
    print 'zipPath:'+zipPath
    print 'extractFold:'+_extractFold
    z =zipfile.ZipFile(zipPath, 'r') 
    z.extractall(_extractFold)
    z.close()
    #删除相关不能更新的文件
    deleteFile(_extractFold+"/assets/data/item/diamondGoodItems.xml")
    #处理各个渠道的更新包
    for channel in channels:
        createChannelUpdateFile(channel,_extractFold,oldTag,targetTag)
#一个渠道的一个差异文件(2个tag之间)    
def createChannelUpdateFile(channelName,extractFold,oldTag,targetTag):
    #添加libApplicationMain.so
    soPath = win_diffAssetsPath+'/libApplicationMain-%s.so'%(channelName)
    soTargetPath = extractFold+'/assets/libApplicationMain.so'
    shutil.copyfile(soPath,soTargetPath)
    #重新打包
    f1 = 'assets'
    f2 = '%s/updatefile/update-%s-%s-%s.zip'%(win_diffAssetsPath,oldTag,targetTag,channelName)
    os.chdir('%s/%s-%s'%(win_diffAssetsPath,oldTag,targetTag))
    compressFold(f1,f2)
#生产所有版本的 所有oldtag，到targetTag的差异文件    
def mergeEveryAssetsSo():
    for tag in oldTags:
        mergeOneAssetsSo(tag,targetTag)
        
if __name__ == '__main__':
    mergeEveryAssetsSo()
     

