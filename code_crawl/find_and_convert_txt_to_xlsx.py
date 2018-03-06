#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from bs4 import BeautifulSoup
import datetime
import time
import xlsxwriter
from selenium import webdriver
import os
import shutil

  
def convert_to_xlsx():

	fopen=open("BIM.txt",'r')  
	lines=fopen.readlines()  
	#新建一个excel文件  
	wb = xlsxwriter.Workbook('prix_action.xlsx')  
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


def download_text():
	# import time
	
	
	driver = webdriver.Chrome()
	driver.get('https://www.abcbourse.com/download/download.aspx?s=BIMp')
	driver.find_element_by_id("ctl00_BodyABC_txtFrom").clear()
	date_action = str(datetime.datetime.now()-datetime.timedelta(days=30)).split(' ')[0].replace('-','/')
	date_action = date_action.split('/')
	jour = date_action[2]
	month = date_action[1]
	year = date_action[0]
	driver.find_element_by_id("ctl00_BodyABC_txtFrom").send_keys(jour+'/'+month+'/'+year)
	driver.find_element_by_id("ctl00_BodyABC_Button1").click()
	# driver.close()

def move_text():
	path_download = 'C:\Users\yja85\Downloads\\'
	path_projet = 'C:\Users\yja85\Desktop\GitHub\projet_finance\code_crawl\\'

	os.chdir(path_download)
	shutil.move(path_download+'BIM.txt', path_projet+'BIM.txt')
	os.chdir(path_projet)



if __name__ == '__main__':
	download_text()
	time.sleep(3)
	move_text()
	time.sleep(3)
	convert_to_xlsx()
	# print(type(datetime.datetime.now()-datetime.timedelta(days=30)))
	# print(str(datetime.datetime.now()-datetime.timedelta(days=30)))
	# a = str(datetime.datetime.now()-datetime.timedelta(days=30)).split(' ')[0].replace('-','/')
	# print(a)