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


class TestSequenceFunctions(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		pass
		
	
		#首页
	# def test_1shouye(self):
		# try:
			# em =comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/act_product_deails_btn_investment')
			# em.click()
			# sleep(1)
			# #项目信息
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/investment_fanben')
			# comdriver.swipe_Up(100)
			# comdriver.swipe_Down(100)
			# comdriver.swipe_Up(100)
			# comdriver.swipe_Down(100)
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			# #安全保障
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/investment_xiangmuxiangqing')
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			# #标的组成
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/investment_jiekuanren')
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			# #已购买记录
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/lendrecord')
			# comdriver.swipe_Down(100)
			# comdriver.swipe_Down(100)
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')

			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/act_product_deails_btn_investment')
			# sleep(2)
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/nowinvest')
			# #确认加入
			# #comdriver.driver_find_by_id('com.sxsfinance.SXS:id/invest').click()
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			# comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')

		# except :
			# print '没有小沙精选'
			# sleep(3)

		#产品
	# def test_2product(self):
	# 	sleep(2)
	# 	comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'产品')]")
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
		sleep(2)
		comdriver.driver.implicitly_wait(4)
		comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'我的')]")
		
		try:
			em =comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/login_btn')
			phone = raw_input('enter your phone:')
			comdriver.driver_find_by_id_keys('com.sxsfinance.SXS:id/login_phone',phone)
			passwd = raw_input('enter your password:')
			comdriver.driver_find_by_id_keys('com.sxsfinance.SXS:id/login_password',passwd)
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/login_btn')
		except:
			
			#我的资产总额
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_total_sum')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_set_button')
			#设置
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_set_button')
			#存管按钮
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_deposit')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/mytips_close')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_ca')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/mytips_close')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_bindcard')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/mytips_close')

			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#昨日利息
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_left_top')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#累计利息
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_right_top')
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#红包
			comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'红包金额')]")
			comdriver.swipe_Left(100)
			comdriver.swipe_Right(100)
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#邀请
			comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'邀请返现')]")
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#小沙
			comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'小沙精选记录')]")
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#四方化缘
			comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'四方化缘记录')]")
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#债权出让
			comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'债权出让')]")
			comdriver.swipe_Left(100)
			comdriver.swipe_Left(100)
			comdriver.swipe_Right(100)
			comdriver.swipe_Right(100)
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			#资金流水
			comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'资金流水')]")
			comdriver.swipe_Left(100)
			comdriver.swipe_Left(100)
			comdriver.swipe_Right(100)
			comdriver.swipe_Right(100)
			comdriver.driver_find_by_id('com.sxsfinance.SXS:id/my_return_button')
			print '333'
			
			
			
	# # 发现
	# def test_4dis(self):
	# 	sleep(2)
	# 	comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'发现')]")



	#注册
	# def test_regist(self):
		# comdriver.driver_find_by_xpath("//android.widget.TextView[contains(@text,'我的')]")
		# try:
			# em =comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/login_btn')
			
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/register_account').click()
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/edttxt_register_phong').send_keys('13521137773')
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/btn_phone_code').click()
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/edttxt_register_code').send_keys('111111')
			# update_db_code()
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/btn_regiter').click()
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/act_update_psd_newps_set_password_edittext').send_keys('123456')
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/act_update_psd_newps_set_new_password_edittext').send_keys('123456')
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/act_update_newps_password_button').click()
			# sleep(2)
			# comdriver.driver.find_element_by_id('com.sxsfinance.SXS:id/act_gesture_verify_tvJumpOver').click()
			# sleep(3)	
		# except:
			# print '3333'
			# comdriver.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'产品')]").click()
	


	
	
	@classmethod
	def tearDownClass(self):
		comdriver.driver.quit()
	



if __name__ =="__main__":

	
	
	
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
	unittest.TextTestRunner(verbosity=2).run(suite)
	#unittest.main()