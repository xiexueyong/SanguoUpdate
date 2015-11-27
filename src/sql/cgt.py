# -*- coding:utf-8 -*-
#! /usr/bin/python

excelpath = u'E:/workspace/PtSanguo_SVN/releaseFold2/updatefile/'    #u'E:\Walls of the world\Excel-content\\'
excelnames = [u'core_update',u'core_channel']# core_upgrade
startrow = 2#起始行
startcolumn = 1#起始列
#sheet_columns= {u'A1':u'id',u'B1':u'title',u'C1':u'slug',u'D1':u'version'} #channel
#sheet_columns= {u'A1':u'id',u'B1':u'channel_id',u'C1':u'cversion',u'D1':u'tversion',u'E1':u'url',u'F1':u'sign',u'G1':u'created_at'}
#sheet_columns= {u'A1':u'id',u'B1':u'channel_id',u'C1':u'version',u'D1':u'url',u'E1':u'md5',u'F1':u'created_at'} #update

DATA_HOST =  u'120.132.91.101'# u'192.168.1.44' '127.0.0.1'  '120.132.91.101'
DATA_USER =  'deploy'#u'deploy' #postgres
DATA_PASSWORD = 'asdf12345678'#u'asdf12345678' #541788
DATA_DBNAME = 'ptkzone'
DATA_PORT = 5432
