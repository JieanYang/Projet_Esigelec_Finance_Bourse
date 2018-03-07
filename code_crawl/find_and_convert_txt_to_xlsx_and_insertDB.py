#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from bs4 import BeautifulSoup
import datetime
import time
import xlsxwriter
from selenium import webdriver
import os
import shutil

import MySQLdb
import xlrd
import datetime

bourse_name = ['Sopra Steria Group', 'Korian', 'Airbus', 'L_oreal', 'Biomerieux']
bourse_link = {'Sopra Steria Group': 'https://www.abcbourse.com/download/download.aspx?s=SOPp',\
				'Korian': 'https://www.abcbourse.com/download/download.aspx?s=KORIp',\
				'Airbus': 'https://www.abcbourse.com/download/download.aspx?s=AIRp',\
				'L_oreal': 'https://www.abcbourse.com/download/download.aspx?s=ORp',\
				'Biomerieux': 'https://www.abcbourse.com/download/download.aspx?s=BIMp'}
bourse_file_name = {'Sopra Steria Group': 'SOP',\
					'Korian': 'KORI',\
					'Airbus': 'AIR',\
					'L_oreal': 'OR',\
					'Biomerieux': 'BIM'}
bourse_code = {'FR0000050809': 'Sopra Steria Group',\
				'FR0010386334': 'Korian',\
				'NL0000235190': 'Airbus',\
				'FR0000120321': 'L_oreal',\
				'FR0013280286': 'Biomerieux'}
  

def convert_to_xlsx(nom):
	fopen=open(bourse_file_name[nom] + ".txt",'r')  
	lines=fopen.readlines()  
	#新建一个excel文件  
	wb = xlsxwriter.Workbook('prix_action_' + bourse_file_name[nom] + '.xlsx')  
	#新建一个sheet  
	sheet = wb.add_worksheet('data')  
	  
	############################  
	# write
	labels = ['code','date','ouverture','haut','bas','dernier','volume']
	sheet.write_row(0,0,labels)
	i = 1
	for line in lines:
		# print type(line)
		data = line.split(";")
		sheet.write_row(i,0,data)
		i = i + 1

	wb.close()
	fopen.close()

	path_projet = 'C:\Users\yja85\Desktop\GitHub\projet_finance\code_crawl\\'
	os.chdir(path_projet)
	os.remove(bourse_file_name[nom] + '.txt')


def download_text(nom):
	# import time
	
	
	driver = webdriver.Chrome()
	driver.get(bourse_link[nom])
	driver.find_element_by_id("ctl00_BodyABC_txtFrom").clear()

	date_action = str(datetime.datetime.now()-datetime.timedelta(days=30)).split(' ')[0].replace('-','/')
	date_action = date_action.split('/')
	jour = date_action[2]
	month = date_action[1]
	year = date_action[0]
	driver.find_element_by_id("ctl00_BodyABC_txtFrom").send_keys(jour+'/'+month+'/'+year)

	driver.find_element_by_id("ctl00_BodyABC_Button1").click()
	# driver.close()

def move_text(nom):
	path_download = 'C:\Users\yja85\Downloads\\'
	path_projet = 'C:\Users\yja85\Desktop\GitHub\projet_finance\code_crawl\\'

	os.chdir(path_download)
	shutil.move(path_download + bourse_file_name[nom] + '.txt', path_projet + bourse_file_name[nom] + '.txt')
	os.chdir(path_projet)

def insert_db():
	db = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="", db="bdd_if")
	cursor = db.cursor()

	cursor.execute("DELETE FROM ressources")


	for i in range(5):
		# -----------------------------------------------------------------
		# data dans xlsx
		data = xlrd.open_workbook('prix_action_' + bourse_file_name[bourse_name[i]] +'.xlsx')
		table = data.sheet_by_name(u'data')
		nrows = table.nrows

		for i in range(nrows-1):
			prix_day_action = table.row_values(i+1)
			# print(prix_day_action)
		# -----------------------------------------------------------------
			date_split = prix_day_action[1].split('/')
			date = datetime.date(int(date_split[2].encode('utf-8'))+2000, int(date_split[1].encode('utf-8')), int(date_split[0].encode('utf-8')))
			
			sql = "INSERT INTO ressources (nom_action, date_action, ouverture, haut, bas, dernier, volume)\
			 VALUES ('" + bourse_code[prix_day_action[0]] + "', '" + date.strftime('%Y-%m-%d') + "', %f, %f, %f, %f, %d)" % \
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

def main(nom):
	download_text(nom)
	time.sleep(3)
	move_text(nom)
	time.sleep(3)
	convert_to_xlsx(nom)

if __name__ == '__main__':
	print('Star . . .')
	for i in range(5):
		main(bourse_name[i])
	insert_db()
	print('finished');


	# print(type(datetime.datetime.now()-datetime.timedelta(days=30)))
	# print(str(datetime.datetime.now()-datetime.timedelta(days=30)))
	# a = str(datetime.datetime.now()-datetime.timedelta(days=30)).split(' ')[0].replace('-','/')
	# print(a)