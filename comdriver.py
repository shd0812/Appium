#coding:utf-8
from appconfig import appium_start
from subprocess import Popen
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
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
	
class Element:

	def __init__(self,element_name):
		self.element_name = element_name
		
	def get_element(self,keys=''):
		element = 'com.sxsfinance.SXS:id'
		try:
			if self.element_name.find(element) == 0:
				if keys.strip() =='':
					driver.find_element_by_id(self.element_name).click()
					sleep(0.5)
				else:
					driver.find_element_by_id(self.element_name).clear()
					driver.find_element_by_id(self.element_name).send_keys(keys)
					sleep(0.5)
				#elements = driver.find_element_by_id(self.element_name)
				
			else:
				elements = driver.find_element_by_xpath(self.element_name).click()
				sleep(0.5)
		except TimeoutException as msg:
			elements = driver.find_element_by_xpath(self.element_name).click()
			print u'查找元素超时%s' % msg
			
	def is_exit(self):
		try:
			el = driver.find_element_by_id(self.element_name)
			return el
		except NoSuchElementException as msg:
			print u'查找元素异常%s' % msg
	
	
