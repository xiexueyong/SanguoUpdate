# -*- coding:utf-8 -*-
#! /bin/usr/python

#import psycopg2

import sys
import sqlfilewrite

reload(sys)
#sys.setdefaultencoding( "utf-8" )

def sqlWriteHandleChannel(DSHcontent,sqlurl,excelname):
    id = str(DSHcontent[0]).strip()
    title = str(DSHcontent[1]).strip()
    slug = str(DSHcontent[2]).strip()
    version = str(DSHcontent[3]).strip()
    version2 = str(DSHcontent[4]).strip()


    #print 3333,beautyid,type(beautyid)
    deleteQuery = u"delete from "+excelname+u" where id = %s ;"
    deleteparams = (id)
    deletesql = deleteQuery % deleteparams
    insertQuery = u"insert into "+excelname+u"(id,title,slug,version,version2) values (%s,'%s','%s','%s','%s') ;"
    insertparams = (id,title,slug,version,version2)
    insertsql = insertQuery % insertparams
    print  'insertsql:',insertsql
    sqlfilewrite.filewritesql(sqlurl,deletesql+'\n')
    sqlfilewrite.filewritesql(sqlurl,insertsql+'\n')


def sqlWriteHandleUpDate(DSHcontent,sqlurl,excelname):
    id = str(DSHcontent[0]).strip()
    channel_id = str(DSHcontent[1]).strip()
    cversion = str(DSHcontent[2]).strip()
    tversion = str(DSHcontent[3]).strip()
    url = str(DSHcontent[4]).strip()
    sign = str(DSHcontent[5]).strip()
    created_at = str(DSHcontent[6]).strip()


    #print 3333,beautyid,type(beautyid)
    deleteQuery = u"delete from "+excelname+u" where id = %s ;"
    deleteparams = (id)
    deletesql = deleteQuery % deleteparams
    insertQuery = u"insert into "+excelname+u"(id,channel_id,cversion,tversion,url,sign,created_at) values (%s,%s,'%s','%s','%s','%s','%s') ;"
    insertparams = (id,channel_id,cversion,tversion,url,sign,created_at)
    insertsql = insertQuery % insertparams
    print  'insertsql:',insertsql
    sqlfilewrite.filewritesql(sqlurl,deletesql+'\n')
    sqlfilewrite.filewritesql(sqlurl,insertsql+'\n')


def sqlWriteHandleUpGrade(DSHcontent,sqlurl,excelname):
    id = str(DSHcontent[0]).strip()
    channel_id = str(DSHcontent[1]).strip()
    version = str(DSHcontent[2]).strip()
    url = str(DSHcontent[3]).strip()
    md5 = str(DSHcontent[4]).strip()
    created_at = str(DSHcontent[5]).strip()


    #print 3333,beautyid,type(beautyid)
    deleteQuery = u"delete from "+excelname+u" where id = %s ;"
    deleteparams = (id)
    deletesql = deleteQuery % deleteparams
    insertQuery = u"insert into "+excelname+u"(id,channel_id,version,url,md5,created_at) values (%s,%s,'%s','%s','%s','%s') ;"
    insertparams = (id,channel_id,version,url,md5,created_at)
    insertsql = insertQuery % insertparams
    print  'insertsql:',insertsql
    sqlfilewrite.filewritesql(sqlurl,deletesql+'\n')
    sqlfilewrite.filewritesql(sqlurl,insertsql+'\n')



