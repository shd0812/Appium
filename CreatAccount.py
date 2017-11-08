#coding:utf-8
import comdriver
from getregist import update_db_code
from time import sleep


def action1(phone,idcard):
	comdriver.driver.implicitly_wait(4)
	el = comdriver.Element("//android.widget.TextView[contains(@text,'我的')]")
	el.get_element()
	if comdriver.Element('com.sxsfinance.SXS:id/login_btn').is_exit():
		
		comdriver.Element('com.sxsfinance.SXS:id/register_account').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/edttxt_register_phong').get_element(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_phone_code').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/edttxt_register_code').get_element('111111')
		update_db_code(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_regiter').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/act_update_psd_newps_set_password_edittext').get_element('123456')
		comdriver.Element('com.sxsfinance.SXS:id/act_update_psd_newps_set_new_password_edittext').get_element('123456')
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
		comdriver.Element('com.sxsfinance.SXS:id/edttxt_register_code').get_element('111111')
		update_db_code(phone)
		comdriver.Element('com.sxsfinance.SXS:id/btn_regiter').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/act_update_psd_newps_set_password_edittext').get_element('123456')
		comdriver.Element('com.sxsfinance.SXS:id/act_update_psd_newps_set_new_password_edittext').get_element('123456')
		comdriver.Element('com.sxsfinance.SXS:id/act_update_newps_password_button').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/act_gesture_verify_tvJumpOver').get_element()
	
		sleep(1)
	if comdriver.Element('com.sxsfinance.SXS:id/sing_next_step').is_exit():
		comdriver.Element('com.sxsfinance.SXS:id/sing_next_step').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/user_name').get_element(u'瞄MIAO')
		# shen fenzheng 
		comdriver.Element('com.sxsfinance.SXS:id/id_card').get_element(idcard)
		comdriver.Element('com.sxsfinance.SXS:id/selectlayout').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/checkBox').get_element()
		comdriver.Element('com.sxsfinance.SXS:id/bank_card_num').get_element('6228480402564890018')
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
	action1('18700113354','430101199901013232')