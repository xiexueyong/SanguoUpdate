#! /usr/bin/env python
# -*- coding: utf-8 -*-

import channelSwitch

def switch():
    print "\n---------------------------------"
    print u"1    移动"
    print u"2    小米"
    print u"3    阿里"
    print u"4    乐视"
    print u"5    葡萄"
    print u"6    爱游戏"
    print u"7    当贝"
    print "-1   Exit"

    print "\n---------------------------------"
    r_input = raw_input("Please make your decision: ")
    channelSwitch.switch(r_input)


switch()