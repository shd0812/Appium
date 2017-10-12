#coding:utf-8
from appconfig import appium_start
from subprocess import Popen
from time import sleep

Popen(' D:/Python/Appium/server/stopAppium.bat',shell = True)
sleep(4)
	
Popen('D:/Python/Appium/server/startAppium.bat',shell = True)
driver= appium_start()

def getSize():
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return (x, y)
#屏幕向上滑动
def swipe_Up(t):
	l = getSize()
	x1 = int(l[0] * 0.5)	#x坐标
	y1 = int(l[1] * 0.75)	#起始y坐标
	y2 = int(l[1] * 0.25)	#终点y坐标
	driver.swipe(x1, y1, x1, y2,t)
#屏幕向下滑动
def swipe_Down(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)	
#屏幕向左滑动
def swipe_Left(t):
	l=getSize()
	x1=int(l[0]*0.75)
	y1=int(l[1]*0.5)
	x2=int(l[0]*0.05)
	driver.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipe_Right(t):
	l=getSize()
	x1=int(l[0]*0.05)
	y1=int(l[1]*0.5)
	x2=int(l[0]*0.75)
	driver.swipe(x1,y1,x2,y1,t)


def driver_find_by_id(sid):
	driver.find_element_by_id(sid).click()
	sleep(0.5)
	
def driver_find_by_xpath(sid):
	driver.find_element_by_xpath(sid).click()
	sleep(0.5)

def driver_find_by_id_keys(sid,keys):
	driver.find_element_by_id(sid).send_keys(keys)
	sleep(0.5)