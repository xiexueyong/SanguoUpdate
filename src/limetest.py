#! /usr/bin/env python
# -*- coding: utf-8 -*-

from limebuildSerially import *

def limetest():
    print "\n---------------------------------"
    print u"1    移动"
    print u"2    小米"
    print u"3    阿里"
    print u"4    乐视"
    print u"5    葡萄"
    print u"6    爱游戏"
    print "-1   Exit"
    print "\n---------------------------------"
    _type = raw_input("Please make your decision: ")

    for channel in channelIndex:
        if channelIndex[channel]==int(_type):
            createApkSoFlash(channelIndex[channel],channel)     
limetest()