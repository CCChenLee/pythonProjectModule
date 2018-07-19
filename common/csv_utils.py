#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#CSV文件操作工具

import csv

#将数据写入CSV文件
def write_csv_file(path,head,data):
	try:
		with open(path,'w',newline='')as csv_file:
			writer=csv.writer(csv_file,dialect='execl')
			if head is not None:
				writer.writerow(head)
			for row in data:
				write.writerow(row)
			print("Write a CSV file to path %s Successful."%path)
	except Exception as e:
		print("Write an CSV file to path:%s,Case:%s"%(path,e))