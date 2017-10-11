#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver

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


def appium_start():
	config = {
		'platformName':'Android',					   #平台
		'platformVersion':'4.4.2',					#系统版本
		'deviceName':'emulator-5554',						 #测试设备ID
		#'deviceName':'T8HMKVSO99999999',
		'appPackage':'com.sxsfinance.SXS',
		'appActivity':'.actvity.main.MainActivity1',
		#'app':'/Users/xiaohutu/GitHub/Android-Test/com.jiuai.apk',		 #apk路径
		#'app':'D:\com.jiuai.apk',
		'newCommandTimeout':30,	   
		'automationName': 'Appium',
		'unicodeKeyboard':True,
		#编码,可解决中文输入问题
		'resetKeyboard':True}
	return webdriver.Remote('http://localhost:4723/wd/hub', config)
#appium_start()



	
