#coding:utf-8
import comdriver
from getregist import update_db_code
from time import sleep
import subprocess
import time

def fast_input(str,element):
    '快速输入'
    x = subprocess.check_output('adb devices', shell=True).split('\n')[1][:-7]
    element.click()
    time.sleep(0.3)
    subprocess.Popen('adb -s %s shell input text %s'%(x,str), shell=True)
    time.sleep(0.5)

def action1(phone,idcard,name):
	comdriver.driver.implicitly_wait(4)
	el = comdriver.Element("//android.widget.TextView[contains(@text,'我的')]")
	el.get_element()
	if comdriver.Element('com.sxsfinance.SXS:id/login_btn').is_exit():
		
		comdriver.Element('com.sxsfinance.SXS:id/register_account').get_element()
		fast_input(phone,comdriver.sxs_element('com.sxsfinance.SXS:id/edttxt_register_phong'))
		#comdriver.Element('com.sxsfinance.SXS:id/edttxt_register_phong').get_element(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_phone_code').get_element()
		el =   comdriver.sxs_element('com.sxsfinance.SXS:id/edttxt_register_code')    
		fast_input('111111',el)
		#comdriver.Element('com.sxsfinance.SXS:id/edttxt_register_code').get_element('111111')
		update_db_code(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_regiter').get_element()
		fast_input('123456',comdriver.sxs_element('com.sxsfinance.SXS:id/act_update_psd_newps_set_password_edittext'))
		fast_input('123456',comdriver.sxs_element('com.sxsfinance.SXS:id/act_update_psd_newps_set_new_password_edittext'))
		# comdriver.Element('com.sxsfinance.SXS:id/act_update_psd_newps_set_password_edittext').get_element('123456')
		# comdriver.Element('com.sxsfinance.SXS:id/act_update_psd_newps_set_new_password_edittext').get_element('123456')
		comdriver.Element('com.sxsfinance.SXS:id/act_update_newps_password_button').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/act_gesture_verify_tvJumpOver').get_element()
	else:
		comdriver.Element('com.sxsfinance.SXS:id/my_set_button').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/my_logout').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/left_btn_double_dialog').get_element()
		comdriver.Element("//android.widget.TextView[contains(@text,'我的')]").get_element()
		comdriver.Element('com.sxsfinance.SXS:id/register_account').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/edttxt_register_phong').get_element(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_phone_code').get_element()
		el =   comdriver.sxs_element('com.sxsfinance.SXS:id/edttxt_register_code')    
		fast_input('111111',el)
		
		update_db_code(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_regiter').get_element()
		fast_input('123456',comdriver.sxs_element('com.sxsfinance.SXS:id/act_update_psd_newps_set_password_edittext'))
		fast_input('123456',comdriver.sxs_element('com.sxsfinance.SXS:id/act_update_psd_newps_set_new_password_edittext'))
		comdriver.Element('com.sxsfinance.SXS:id/act_update_newps_password_button').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/act_gesture_verify_tvJumpOver').get_element()
	
		sleep(1)
	if comdriver.Element('com.sxsfinance.SXS:id/sing_next_step').is_exit():
		comdriver.Element('com.sxsfinance.SXS:id/sing_next_step').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/user_name').get_element(name)
		
		# shen fenzheng 
		fast_input(idcard,comdriver.sxs_element('com.sxsfinance.SXS:id/id_card'))
		comdriver.Element('com.sxsfinance.SXS:id/selectlayout').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/checkBox').get_element()
		fast_input('6228480402564890018',comdriver.sxs_element('com.sxsfinance.SXS:id/bank_card_num'))
		comdriver.Element('com.sxsfinance.SXS:id/next_btn').get_element()
		sleep(2)
		webview= comdriver.driver.contexts[1]
		comdriver.driver.switch_to.context(webview)
		comdriver.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
		comdriver.driver.find_element_by_xpath('//*[@id="sendSmsVerify"]').click()
		comdriver.driver.find_element_by_xpath('//*[@id="alertLayer"]/div[2]').click()
		comdriver.driver.find_element_by_xpath('//*[@id="smsCode"]').send_keys('123456')
		comdriver.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
		comdriver.driver.find_element_by_xpath('//*[@id="confirmPassword"]').send_keys('123456')
		comdriver.driver.find_element_by_xpath('//*[@id="nextButton"]').send_keys('KeysToSend')
		comdriver.driver.find_element_by_xpath('//*[@id="nextButton"]').click()
		webview1= comdriver.driver.contexts[0]
		comdriver.driver.switch_to.context(webview1)
		sleep(1)
if	__name__ == '__main__':
	action1('13801000011','140105199901012391',u'申14')
	
	sxs_list = [['13801000010','140105199901019294',u'申13'],['13801000011','140105199901012391',u'申14']]
	
	