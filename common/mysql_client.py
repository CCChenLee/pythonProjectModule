#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#
#MySQL连接和操作函数集

from common.conf_utils import ConfigReader

import pymysql
import datetime

#MySQL获取数据库连接
def connect_pool():
	cr=ConfigReader('配置文件绝对路径/db.ini')
	conf=cr.get_mysql_info()

	return pymysql.connections.Connection(host=conf.host,
											port=conf.port,
											user=conf.user,
											password=conf.password,
											database=conf.schema,
											charset=conf.charset)

#MySQL统一数据查询方法
def query_table(sql):
	print('MySQL client query start...')
	start=datetime.datetime.now()
	print(sql)

	result=[]
	try:
		conn=connect_pool()
		cur=conn.cursor()
		cur.exeute(sql)
		for row in cur.fetchall():
			result.append([cell for cell in row])
	except Exception as e:
		print('Query from MySQL table failed.Case:%s\n'%e)
	finally:
		if cur:
			cur.close()
		if conn:
			conn.close()
	records=len(result)

	end=datetime.datetime.now()
	print('MySQL client query completed in %s seconds.Records found:s\n'%((end-start).seconds,records))
	return result

#MySQL统一数据更新
def update_record(sql):
	result=[]
	try:
		conn=connect_pool()
		cur=conn.cursor()
		cur.execute(sql)
	except Exception as e:
		print('update MySQL table failed.Case:%s\n'%e)
	finally:
		conn.commit()
		if cur:
			cur.close()
		if conn:
			conn.close()
	return