#coding:utf-8
import pymysql


def update_db_code(phone):
	db = pymysql.connect(host='192.168.130.203',port=9309\
	,user='root',passwd='sxslocalhost2017'\
	,db='sxs_vault',use_unicode=True,charset='utf8')
	cursor=db.cursor()
	
	#phone = '18700112233'
	# 参数化sql 有 两种方式，一种是字典，另一种是 目前正在用的
	# sql = '''
	   # UPDATE vault_user_mobile_verify SET verify = '56' WHERE mobile = %(phone)s
	   # '''
	   
	# vaule = {"phone":'18700112233'}
	# cursor.execute(sql,vaule)
	
	cursor.execute ("UPDATE vault_user_mobile_verify SET verify = '111111' WHERE mobile = %s",phone)
	db.commit()
	print 'this phone is  %s' % phone
#data = cursor.fetchall()

#data =cursor.fetchone()
	db.close()

	
	
# if __name__ == '__main__':
	# update_db_code('18700112233')
#update_db_code()
#print data