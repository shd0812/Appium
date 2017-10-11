#coding:utf-8
import pymysql


def update_db_code():
    db = pymysql.connect(host='192.168.130.203',port=9309\
	,user='root',passwd='sxslocalhost2017'\
	,db='sxs_vault',use_unicode=True,charset='utf8')
    cursor=db.cursor()


    sql = '''
       UPDATE vault_user_mobile_verify SET verify = '111111' WHERE mobile = '13521137773'
       '''
    cursor.execute(sql)
    db.commit()
#data = cursor.fetchall()

#data =cursor.fetchone()
    db.close()

#update_db_code()
#print data