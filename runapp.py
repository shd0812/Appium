#coding:utf-8
# from sys import path
# path.append('D:/Python/Appium/server')
# import server
#from appconfig import appium_start
#import appconfig
from time import sleep
from appium import webdriver
import unittest
from getregist import update_db_code
from subprocess import Popen
import comdriver
import appiumlog

class TestSequenceFunctions(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.log = comdriver.log
		#添加开始log
		self.log.build_start_line()
		self.log.build_case('open app')
		
		
	
		#首页
	# def test_1shouye(self):
		# try:
			# em =comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/act_product_deails_btn_investment')
			# em.click()
			# sleep(1)
			# #项目信息
			# comdriver.Element('com.sxsfinance.SXS:id/investment_fanben')
			# comdriver.swipe_Up(100)
			# comdriver.swipe_Down(100)
			# comdriver.swipe_Up(100)
			# comdriver.swipe_Down(100)
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')
			# #安全保障
			# comdriver.Element('com.sxsfinance.SXS:id/investment_xiangmuxiangqing')
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')
			# #标的组成
			# comdriver.Element('com.sxsfinance.SXS:id/investment_jiekuanren')
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')
			# #已购买记录
			# comdriver.Element('com.sxsfinance.SXS:id/lendrecord')
			# comdriver.swipe_Down(100)
			# comdriver.swipe_Down(100)
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')

			# comdriver.Element('com.sxsfinance.SXS:id/act_product_deails_btn_investment')
			# sleep(2)
			# comdriver.Element('com.sxsfinance.SXS:id/nowinvest')
			# #确认加入
			# #comdriver.Element('com.sxsfinance.SXS:id/invest').click()
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')
			# comdriver.Element('com.sxsfinance.SXS:id/my_return_button')

		# except :
			# print '没有小沙精选'
			# sleep(3)

		#产品
	# def test_2product(self):
	# 	sleep(2)
	# 	comdriver.Element("//android.widget.TextView[contains(@text,'产品')]")
	# 	comdriver.swipe_Left(100)
	# 	comdriver.swipe_Left(100)
	# 	# comdriver.swipe_Left(100)
	# 	# comdriver.swipe_Right(100)
	# 	# comdriver.swipe_Up(100)
	# 	# comdriver.swipe_Up(100)
	# 	# comdriver.swipe_Up(100)
	# 	# comdriver.swipe_Up(100)
	# 	# comdriver.swipe_Up(100)
	
	# 我的
	def test_3my(self):
		
		self.log.build_case('从首页跳转我的页面')
		comdriver.driver.implicitly_wait(4)
		el = comdriver.Element("//android.widget.TextView[contains(@text,'我的')]")
		
		el.get_element()
		
		if comdriver.Element('com.sxsfinance.SXS:id/login_btn').is_exit():
			self.log.build_case('登录')
			phone = raw_input('enter your phone:')
			comdriver.Element('com.sxsfinance.SXS:id/login_phone').get_element(phone)
			passwd = raw_input('enter your password:')
			comdriver.Element('com.sxsfinance.SXS:id/login_password').get_element(passwd)
			comdriver.Element('com.sxsfinance.SXS:id/login_btn').get_element()
		else:
			print '444444'
			pass
	
		sleep(2)
		 # [u'NATIVE_APP', u'WEBVIEW_com.sxsfinance.SXS']
		 
		self.log.build_case('充值')
		comdriver.Element('com.sxsfinance.SXS:id/my_recharge').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/recharge_edittext').get_element('100')
		comdriver.Element('com.sxsfinance.SXS:id/recharge_button').get_element()
		sleep(3)
		
		webview= comdriver.driver.contexts[1]
		comdriver.driver.switch_to.context(webview)
		sleep(2)
		print comdriver.driver.contexts[1] 
		
		comdriver.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
		comdriver.driver.find_element_by_xpath('//*[@id="nextButton"]').click()
		print '2222222222222321312'
		webview1= comdriver.driver.contexts[0]
		comdriver.driver.switch_to.context(webview1)
		comdriver.Element('com.sxsfinance.SXS:id/my_set_button').get_element()
		
		sleep(4)
		
		print str(comdriver.driver.contexts) +'333333342342342343'
			#我的资产总额
		# self.log.build_case('我的资产总额')
		# comdriver.Element('com.sxsfinance.SXS:id/my_total_sum').get_element()
		# comdriver.Element("//android.widget.TextView[contains(@text,'资金流水')]").get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_set_button').get_element()
		# self.log.build_case('设置')
			#设置
		# comdriver.Element('com.sxsfinance.SXS:id/my_set_button').get_element()
			# #存管按钮
		# comdriver.Element('com.sxsfinance.SXS:id/my_deposit').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/mytips_close').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_ca').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/mytips_close').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_bindcard').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/mytips_close').get_element()

		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #昨日利息
		# self.log.build_case('昨日利息')
		# comdriver.Element('com.sxsfinance.SXS:id/my_left_top').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		
		# #累计利息
		# self.log.build_case('累计利息')
		# comdriver.Element('com.sxsfinance.SXS:id/my_right_top').get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #红包
		# self.log.build_case('红包')
		# comdriver.Element("//android.widget.TextView[contains(@text,'红包金额')]").get_element()
		# comdriver.swipe_Left(100)
		# comdriver.swipe_Right(100)
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #邀请
		# self.log.build_case('邀请')
		# comdriver.Element("//android.widget.TextView[contains(@text,'邀请返现')]").get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #小沙
		# self.log.build_case('小沙')
		# comdriver.Element("//android.widget.TextView[contains(@text,'小沙精选记录')]").get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #四方化缘
		# self.log.build_case('四方化缘页面')
		# comdriver.Element("//android.widget.TextView[contains(@text,'四方化缘记录')]").get_element()
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #债权出让
		# self.log.build_case('债权出让页面')
		# comdriver.Element("//android.widget.TextView[contains(@text,'债权出让')]").get_element()
		# comdriver.swipe_Left(100)
		# comdriver.swipe_Left(100)
		# comdriver.swipe_Right(100)
		# comdriver.swipe_Right(100)
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		# #资金流水
		# self.log.build_case('资金流水页面')
		# comdriver.Element("//android.widget.TextView[contains(@text,'资金流水')]").get_element()
		# comdriver.swipe_Left(100)
		# comdriver.swipe_Left(100)
		# comdriver.swipe_Right(100)
		# comdriver.swipe_Right(100)
		# comdriver.Element('com.sxsfinance.SXS:id/my_return_button').get_element()
		
		print '333'
			
			
			
	# # 发现
	# def test_4dis(self):
	# 	sleep(2)
	# 	comdriver.Element("//android.widget.TextView[contains(@text,'发现')]")



	
	


	
	
	@classmethod
	def tearDownClass(self):
		self.log.build_case('kill app')
		self.log.build_end_line()
		comdriver.driver.quit()
	



if __name__ =="__main__":

	
	
	
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
	unittest.TextTestRunner(verbosity=2).run(suite)
	#unittest.main()