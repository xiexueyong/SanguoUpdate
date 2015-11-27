#! /usr/bin/env python
# -*- coding: utf-8 -*-

#是否是调试版so
debug = True;
#版本tag集合
alltags = ['v1.5.6d','v1.5.7d','v1.5.8d','v1.5.9d','v1.5.10d','v1.5.11d','v1.5.12d','v1.5.13d','v1.5.15d','v1.5.16d','v1.5.17d','v1.5.18d']
#所有的渠道名
channels = ['putaogame','lovegame']
#用于切换渠道
channelIndex= {'chinamobile':1,'xiaomi':2,'ali':3,'letv':4,'putaogame':5,'lovegame':6,'dangbei':7}
oldTags = alltags[0:len(alltags)-1]
targetTag = alltags[len(alltags)-1]
#用不同更新素材的渠道id集合,1,3,37三个id废弃不用
whoUseLetv=[4]
whoUseChinamobile=[5]
whoUseLovegame=[6]
whoUseAli=[84]
whoUseXiaomi=[83]
whoUsePutao=[23,58,71,66]
#存储所有的使用关系
useRelation = {'lovegame':whoUseLovegame,'ali':whoUseAli,'chinamobile':whoUseChinamobile,'xiaomi':whoUseXiaomi,'putaogame':whoUsePutao,'letv':whoUseLetv}
#idHead从1或者100000开始，防止在本次更新期间有玩家升级上次的小更新。
idHead = 2320#上次是1438

projectPath = '/cygdrive/e/workspace/PtSanguo_SVN'#项目目录
diffAssetsPath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold2'#存放差异文件的目录
updateFilePath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold2/updatefile'#存放合并后差异文件的目录
apkPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"#编译出来的原生apk路径
soPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"#编译出来的so路径
targetApkPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold2"#存放apk的目录
targetSoPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold2"#存放so的目录

win_projectPath = 'e:/workspace/PtSanguo_SVN'
win_diffAssetsPath = 'e:/workspace/PtSanguo_SVN/releaseFold2'
win_updateFilePath = 'e:/workspace/PtSanguo_SVN/releaseFold2/updatefile'
win_apkPath = "E:/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"
win_soPath = "E:/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"
win_targetApkPath = "E:/workspace/PtSanguo_SVN/releaseFold2"
win_targetSoPath = "E:/workspace/PtSanguo_SVN/releaseFold2"
win_swfPath = "C:/tomcat6/webapps/ROOT/flash/bin/PtSanguo.swf"#编译出来的原生swf路径
win_channelApkPath = 'e:/workspace/PtSanguo_SVN/releaseFold2'#存放打完皮后的apk

preFtpURL='http://ptkingdom.b0.upaiyun.com/up/update/'#ftp文件下载地址前缀
apkPreFtpURL='http://ptkingdom.b0.upaiyun.com/up/upgrade/'#ftp文件下载地址前缀
#preFtpURL='http://192.168.1.198:8080/'

