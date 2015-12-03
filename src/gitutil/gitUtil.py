#-*- coding:utf-8 -*-
#!/bin/usr/python
import os
import os.path

def getCurBranch():
    os.chdir('E:/workspace/PtSanguo_SVN')
    lines = os.popen('git branch -a').readlines()
    
    for line in lines:
        p = line.find('*')
        if p>=0:
           b = line[p+2:]
           return b.strip()
    return None