#! /usr/bin/env python
# -*- coding: utf-8 -*-

import md5
import os

def getMD5(fp):
    m = md5.new()
    a_file = open(fp, 'rb')    
    m.update(a_file.read())
    a_file.close()
    
    global allmd5
    md5Str = m.hexdigest()
    return md5Str

    

    
    
