#! /usr/bin/env python
# -*- coding: utf-8 -*-
from gitutil import gitUtil # getCurBranch

branch='allp'# 'allp' 'mobileupdate'
if gitUtil.getCurBranch() != branch:
    print '不在指定的分支，请重新指定分支'
    branch='错误'
else:
    print '为%s分支打包'%(branch)
    
if branch=='allp':
    #是否是调试版so
    debug = False;
    #版本tag集合
    #alltags = ['v2.0.0b','v2.0.1b','v2.0.2b','v2.0.3b','v2.0.4b','v2.0.5b','v2.0.6b','v2.0.7b','v2.0.8b','v2.0.9b']
    alltags = ['v3.0.0b','v3.0.1b']
    #所有的渠道名
    channels = ['unicom','wangsu','lovegame','putaogame','dangbei','xiaomi','ali','chinamobile','letv','atet','phone']#'cybercloud','ysten',
    #channels = ['ysten']
    #用于切换渠道
    channelIndex= {'chinamobile':1,'xiaomi':2,'ali':3,'letv':4,'putaogame':5,'lovegame':6,'dangbei':7,'atet':8,'cybercloud':9,'ysten':10,'phone':11,'unicom':12,'wangsu':13}
    oldTags = alltags[0:len(alltags)-1]
    targetTag = alltags[len(alltags)-1]
    #用不同更新素材的渠道id集合,37,88三个id废弃不用
    whoUseLetv=[4]
    whoUseAtet=[16]
    whoUseChinamobile=[5]
    whoUseLovegame=[6,3]
    whoUseDangbei=[33]
    whoUseAli=[84]
    whoUseXiaomi=[83]
    whoUsePhone=[37,99]
    whoUseUnicom=[97]
    whoUseWangsu=[98]
    whoUsePutao=[1,2,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,38,
    39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,
    72,73,74,75,76,77,78,79,80,81,82,85,86,87,89,90,91,92,93,100]
    useRelation = {'lovegame':whoUseLovegame,'ali':whoUseAli,'chinamobile':whoUseChinamobile,'xiaomi':whoUseXiaomi,'putaogame':whoUsePutao,'letv':whoUseLetv,'dangbei':whoUseDangbei,'atet':whoUseAtet,'phone':whoUsePhone,'unicom':whoUseUnicom,'wangsu':whoUseWangsu}
    #idHead从1或者100000开始，防止在本次更新期间有玩家升级上次的小更新。
    idHead = 53998#上次是1438
    
    projectPath = '/cygdrive/e/workspace/PtSanguo_SVN'#项目目录
    diffAssetsPath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold3'#存放差异文件的目录
    updateFilePath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold3/updatefile'#存放合并后差异文件的目录
    apkPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"#编译出来的原生apk路径
    soPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"#编译出来的so路径
    targetApkPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold3"#存放apk的目录
    targetSoPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold3"#存放so的目录
    
    win_projectPath = 'e:/workspace/PtSanguo_SVN'
    win_diffAssetsPath = 'e:/workspace/PtSanguo_SVN/releaseFold3'
    win_updateFilePath = 'e:/workspace/PtSanguo_SVN/releaseFold3/updatefile'
    win_apkPath = "E:/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"
    win_soPath = "E:/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"
    win_targetApkPath = "E:/workspace/PtSanguo_SVN/releaseFold3"
    win_targetSoPath = "E:/workspace/PtSanguo_SVN/releaseFold3"
    win_swfPath = "C:/tomcat6/webapps/ROOT/flash/bin/PtSanguo.swf"#编译出来的原生swf路径
    win_channelApkPath = 'e:/workspace/PtSanguo_SVN/releaseFold3'#存放打完皮后的apk
    
    preFtpURL='http://ptkingdom.b0.upaiyun.com/up/update/'#ftp文件下载地址前缀
    apkPreFtpURL='http://ptkingdom.b0.upaiyun.com/up/upgrade/'#ftp文件下载地址前缀
    #preFtpURL='http://192.168.1.198:8080/'
elif branch=='mobileupdate':
    #是否是调试版so
    debug = False;
    #版本tag集合
    alltags = ['v1.5.0b','v1.5.1b','v1.5.2b','v1.5.3b','v1.5.4b','v1.5.7b','v1.5.8b','v1.5.10b','v1.5.11b','v1.5.12b','v1.5.13b','v1.5.14b','v1.5.15b','v1.5.16b','v1.5.17b','v1.5.18b','v1.5.19b','v1.5.20b','v1.5.21b','v1.5.22b','v1.5.25b','v1.5.26b','v1.5.27b','v1.5.29b','v1.5.30b','v1.5.31b','v1.5.32b','v1.5.33b','v1.5.34b','v1.5.35b','v1.5.36b']
    #所有的渠道名
    #channels = ['lovegame','putaogame','dangbei','xiaomi','ali','chinamobile','letv','atet']
    channels = ['chinamobile']
    #用于切换渠道
    channelIndex= {'chinamobile':1,'xiaomi':2,'ali':3,'letv':4,'putaogame':5,'lovegame':6,'dangbei':7,'atet':8}
    oldTags = alltags[0:len(alltags)-1]
    targetTag = alltags[len(alltags)-1]
    #用不同更新素材的渠道id集合,37,88三个id废弃不用
    whoUseChinamobile=[5]
    #存储所有的使用关系
    useRelation = {'chinamobile':whoUseChinamobile}
    #idHead从1或者100000开始，防止在本次更新期间有玩家升级上次的小更新。
    idHead = 53965#上次是1438
    
    projectPath = '/cygdrive/e/workspace/PtSanguo_SVN'#项目目录
    diffAssetsPath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold4'#存放差异文件的目录
    updateFilePath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold4/updatefile'#存放合并后差异文件的目录
    apkPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"#编译出来的原生apk路径
    soPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"#编译出来的so路径
    targetApkPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold4"#存放apk的目录
    targetSoPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold4"#存放so的目录
    
    win_projectPath = 'e:/workspace/PtSanguo_SVN'
    win_diffAssetsPath = 'e:/workspace/PtSanguo_SVN/releaseFold4'
    win_updateFilePath = 'e:/workspace/PtSanguo_SVN/releaseFold4/updatefile'
    win_apkPath = "E:/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"
    win_soPath = "E:/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"
    win_targetApkPath = "E:/workspace/PtSanguo_SVN/releaseFold4"
    win_targetSoPath = "E:/workspace/PtSanguo_SVN/releaseFold4"
    win_swfPath = "C:/tomcat6/webapps/ROOT/flash/bin/PtSanguo.swf"#编译出来的原生swf路径
    win_channelApkPath = 'e:/workspace/PtSanguo_SVN/releaseFold4'#存放打完皮后的apk
    
    preFtpURL='http://ptkingdom.b0.upaiyun.com/up/update/'#ftp文件下载地址前缀
    apkPreFtpURL='http://ptkingdom.b0.upaiyun.com/up/upgrade/'#ftp文件下载地址前缀
    #preFtpURL='http://192.168.1.198:8080/'

