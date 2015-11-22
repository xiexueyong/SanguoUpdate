#-*- coding:utf-8 -*-
#!/bin/usr/python



def filewritesql(filepath,writecontent):
    filewrite = open(filepath,'a')
    try:
        filewrite.write(writecontent.encode('utf-8'))
    finally:
        filewrite.close()
