#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import shutil 
import os.path 

from GlobalConfig import *
from copyfile import *
#_cwd = os.getcwd()
#workPath = os.path.split(_cwd)[0]+'/'
#workPath = 'E:/workspace/PtSanguo_SVN/'
#print "workPath:"+workPath


def mobileProject():
    #asset资源
    print u"asset资源替换\n"
    mAssetSourcePath =win_projectPath+"/plateformFile/plateformassets/assets_chinamobile/"
    mAssetTargetPath =win_projectPath+"/templates/android/template/assets/"
    assetCopy(mAssetSourcePath,mAssetTargetPath)
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_chinamobile.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_mobile.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    #"plateformFile/handler/PTHandler.java
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath+"/plateformFile/handler/PTHandler.java_putao"
    mPThandlerTargetPath = win_projectPath+"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
	
	#diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_chinaMobile.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)

def aliProject():
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_ali.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_ali.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath+"/plateformFile/handler/PTHandler.java_ali"
    mPThandlerTargetPath = win_projectPath+"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
	
	#diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_ali.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)
    
def letvProject():
    print u"asset资源替换\n"
    #asset资源
    mAssetSourcePath =win_projectPath+"/plateformFile/plateformassets/assets_letv/"
    mAssetTargetPath =win_projectPath+"/templates/android/template/assets/"
    assetCopy(mAssetSourcePath,mAssetTargetPath)
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_letv.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_letv.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath+"/plateformFile/handler/PTHandler.java_letv"
    mPThandlerTargetPath = win_projectPath+"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
	
	#diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_letv.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)
	
def xiaomiProject():
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_xiaomi.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_xiaomi.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath+"/plateformFile/handler/PTHandler.java_putao"
    mPThandlerTargetPath = win_projectPath+"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
	
	#diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_xiaomi.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)
    
def putaoProject():
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_putao.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_putao.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath+"/plateformFile/handler/PTHandler.java_putao"
    mPThandlerTargetPath = win_projectPath+"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
	
	#diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_pt.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)
	
def lovegameProject():
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_lovegame.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_lovegame.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath+"/plateformFile/handler/PTHandler.java_lovegame"
    mPThandlerTargetPath = win_projectPath+"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_aiyouxi.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)
    
def dangbeiProject():
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath+"/plateformFile/manifast/AndroidManifest_dangbei.xml"
    mManifestTargetPath = win_projectPath+"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+"/plateformFile/projectxml/Project_dangbei.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath+"/plateformFile/goodsitems/diamondGoodItems_dangbei.xml"
    mGoodItemsTargetPath = win_projectPath+"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)
    
def atetProject():
    #AndroidManifest替换
    print u"AndroidManifest替换\n"
    mManifestPath = win_projectPath +"/plateformFile/manifast/AndroidManifest_atet.xml"
    mManifestTargetPath = win_projectPath +"/templates/android/template/AndroidManifest.xml"
    manifestModefied(mManifestPath,mManifestTargetPath)
    #project替换
    print u"progect替换\n"
    mProjectPath =win_projectPath+ "/plateformFile/projectxml/Project_atet.xml"
    mProjectTargetPath = win_projectPath+"/Project.xml"
    projectModefied(mProjectPath,mProjectTargetPath)
    #PTHandler.java替换
    print u"PTHandler.java替换\n"
    mPThandlerPath = win_projectPath +"/plateformFile/handler/PTHandler.java_putao"
    mPThandlerTargetPath = win_projectPath +"/templates/android/template/src/com/putao/PtSanguo/PTHandler.java"
    PTHandlerModefied(mPThandlerPath,mPThandlerTargetPath)
    #diamondGoodItems.xml
    #"plateformFile/goodsitems/diamondGoodItems.xml
    print u"diamondGoodItems.xml替换\n"
    mGoodItemsPath = win_projectPath +"/plateformFile/goodsitems/diamondGoodItems_atet.xml"
    mGoodItemsTargetPath = win_projectPath +"/assets/data/item/diamondGoodItems.xml"
    GoodsItemsModefied(mGoodItemsPath,mGoodItemsTargetPath)

    
def assetCopy(sourceDir,targetDir):
    copyFiles(sourceDir,targetDir)

def manifestModefied(sourceDir,targetDir):
    shutil.copyfile(sourceDir,targetDir)

def PTHandlerModefied(sourceDir,targetDir):
    shutil.copyfile(sourceDir,targetDir)
def GoodsItemsModefied(sourceDir,targetDir):
    #shutil.copyfile(sourceDir,targetDir)
    pass

def projectModefied(sourceDir,targetDir):
    shutil.copyfile(sourceDir,targetDir)
def addSensitiveWord():
    swPath = win_projectPath+"/plateformFile/plateformassets/sensitiveWord.txt"
    swTargetPath = win_projectPath+"/templates/android/template/assets/sensitiveWord.txt"
    shutil.copyfile(swPath,swTargetPath)

def clearProject():
    templateAssets = win_projectPath+"/templates/android/template/assets/"
    if os.path.exists(templateAssets):
        shutil.rmtree(templateAssets) 
        os.mkdir(templateAssets)
    
    exportbin = win_projectPath+"/export/android/bin/"
    if os.path.exists(exportbin):
        shutil.rmtree(exportbin)
		
    addSensitiveWord()
        
               

def switch(type=5):
    clearProject()
    if int(type) == -1:
        print 'Exited!!'
        exit()
    if int(type) == 1:
        print u"开始:%s\n"%(type)
        mobileProject()
        print u"\n完成"
    if int(type) == 2:
        print u"开始:%s\n"%(type)
        xiaomiProject()
        print u"\n完成"
    if int(type) == 3:
        print u"开始:%s\n"%(type)
        aliProject()
        print u"\n完成"
    if int(type) == 4:
        print u"开始:%s\n"%(type)
        letvProject()
        print u"\n完成"
    if int(type) == 5:
        print u"开始:%s\n"%(type)
        putaoProject()
        print u"\n完成"
    if int(type) == 6:
        print u"开始:%s\n"%(type)
        lovegameProject()
        print u"\n完成"
    if int(type) == 7:
        print u"开始:%s\n"%(type)
        dangbeiProject()
        print u"\n完成"
    if int(type) == 8:
        print u"开始:%s\n"%(type)
        atetProject()
        print u"\n完成"


    
