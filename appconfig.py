#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver
import readconfig
#sys.path.append("..")
#用于解决多个手机连接问题
#from common.mobile import get_serialno

#Read mobile deviceId
#device_id = get_serialno()

#Read mobile os Version
#os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()

#appium -a 127.0.0.1 -p 4723  启动appium服务

#如果只是想查看手机上应用的packageName，则输入命令：

#adb shell pm list packages
# .actvity.main.GuidepageActivity	 HomeLoginActivity	 MainActivity1


rc = readconfig.ReadConfig()

#print rc.getVaule('baskurl')

def appium_start():
	config = {
		'platformName':rc.getVaule('platformName'),					  
		'platformVersion':rc.getVaule('platformVersion'),					
		'deviceName':rc.getVaule('deviceName'),						 
		'appPackage':rc.getVaule('appPackage'),
		'appActivity':rc.getVaule('appActivity'),
		'newCommandTimeout':rc.getVaule('newCommandTimeout'),	   
		'automationName': rc.getVaule('automationName'),
		'unicodeKeyboard':rc.getVaule('unicodeKeyboard'),
		'resetKeyboard':rc.getVaule('resetKeyboard')}
	return webdriver.Remote(rc.getVaule('baskurl'), config)
#appium_start()



	
