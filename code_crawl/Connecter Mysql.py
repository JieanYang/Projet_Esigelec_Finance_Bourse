#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import time 
import MySQLdb
import xlrd
import datetime


db = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="", db="bdd_if")
cursor = db.cursor()

# -----------------------------------------------------------------
# data dans xlsx
data = xlrd.open_workbook('prix_action.xlsx')
table = data.sheet_by_name(u'data')
nrows = table.nrows

for i in range(nrows-1):
	prix_day_action = table.row_values(i+1)
	# print(prix_day_action)
# -----------------------------------------------------------------
	date_split = prix_day_action[1].split('/')
	date = datetime.date(int(date_split[2].encode('utf-8'))+2000, int(date_split[1].encode('utf-8')), int(date_split[0].encode('utf-8')))
	
	sql = "INSERT INTO ressources (nom_action, date_action, ouverture, haut, bas, dernier, volume)\
	 VALUES ('" + prix_day_action[0] + "', '" + date.strftime('%Y-%m-%d') + "', %f, %f, %f, %f, %d)" % \
	 (float(prix_day_action[2].encode('utf-8')), float(prix_day_action[3].encode('utf-8')), \
	 	float(prix_day_action[4].encode('utf-8')), float(prix_day_action[5].encode('utf-8')), \
	 	int(prix_day_action[6].encode('utf-8')))

	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		db.commit()
	except:
		db.rollback()
		print('error of sql operation!')


db.close()