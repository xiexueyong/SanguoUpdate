#! /usr/bin/env python
# -*- coding: utf-8 -*-

#是否是调试版so
debug = False;
#版本tag集合
alltags = ['v1.5.0b','v1.5.1b','v1.5.2b','v1.5.3b','v1.5.4b','v1.5.7b','v1.5.8b','v1.5.10b','v1.5.11b','v1.5.12b','v1.5.13b','v1.5.14b','v1.5.15b','v1.5.16b','v1.5.17b','v1.5.18b']
#所有的渠道名
channels = ['putaogame','dangbei','xiaomi','ali','letv','chinamobile']
#用于切换渠道
channelIndex= {'chinamobile':1,'xiaomi':2,'ali':3,'letv':4,'putaogame':5,'lovegame':6,'dangbei':7}
oldTags = alltags[0:len(alltags)-1]
targetTag = alltags[len(alltags)-1]
#用不同更新素材的渠道id集合,1,3,37,88四个id废弃不用
whoUseLetv=[4]
whoUseChinamobile=[5]
whoUseLovegame=[6]
whoUseDangbei=[33]
whoUseAli=[84]
whoUseXiaomi=[83]
whoUsePutao=[2,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,34,35,36,38,
39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,65,67,68,69,70,
72,73,74,75,76,77,78,79,80,81,82,85,86,87,89,90]
#存储所有的使用关系
useRelation = {'ali':whoUseAli,'chinamobile':whoUseChinamobile,'xiaomi':whoUseXiaomi,'putaogame':whoUsePutao,'letv':whoUseLetv,'dangbei':whoUseDangbei}
#useRelation = {'ali':whoUseAli,'chinamobile':whoUseChinamobile,'xiaomi':whoUseXiaomi,'letv':whoUseLetv}
#idHead从1或者100000开始，防止在本次更新期间有玩家升级上次的小更新。
idHead = 10000#上次是10000

projectPath = '/cygdrive/e/workspace/PtSanguo_SVN'#项目目录
diffAssetsPath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold'#存放差异文件的目录
updateFilePath = '/cygdrive/e/workspace/PtSanguo_SVN/releaseFold/updatefile'#存放合并后差异文件的目录
apkPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"#编译出来的原生apk路径
soPath = "/cygdrive/e/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"#编译出来的so路径
targetApkPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold"#存放apk的目录
targetSoPath = "/cygdrive/e/workspace/PtSanguo_SVN/releaseFold"#存放so的目录

win_projectPath = 'e:/workspace/PtSanguo_SVN'
win_diffAssetsPath = 'e:/workspace/PtSanguo_SVN/releaseFold'
win_updateFilePath = 'e:/workspace/PtSanguo_SVN/releaseFold/updatefile'
win_apkPath = "E:/workspace/PtSanguo_SVN/export/android/bin/bin/PtSanguo-release.apk"
win_soPath = "E:/workspace/PtSanguo_SVN/export/android/bin/libs/armeabi/libApplicationMain.so"
win_targetApkPath = "E:/workspace/PtSanguo_SVN/releaseFold"
win_targetSoPath = "E:/workspace/PtSanguo_SVN/releaseFold"
win_swfPath = "C:/tomcat6/webapps/ROOT/flash/bin/PtSanguo.swf"#编译出来的原生swf路径
win_channelApkPath = 'e:/workspace/PtSanguo_SVN/releaseFold'#存放打完皮后的apk

preFtpURL='http://ptkingdom.b0.upaiyun.com/up/update/'#ftp文件下载地址前缀
apkPreFtpURL='http://ptkingdom.b0.upaiyun.com/up/upgrade/'#ftp文件下载地址前缀
#preFtpURL='http://192.168.1.198:8080/'

