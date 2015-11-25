# -*- coding: utf-8 -*-
#读logcat文件
#查找某个字符并打印该行
import os
import sys
import datetime,time
import linecache
import codecs
logcatfilepath = os.path.split(os.path.realpath(__file__))[0]
name=input("please check in logcatname: ")
logcatname=logcatfilepath+'\\'+name+'.log'

#1.获取文件行号
#...
rowsum = len(codecs.open(logcatname, 'rU', 'utf-8').readlines())-1

#2.查找每一行是否有字符
def seachstr(strname,rownum):
	str0= linecache.getline(logcatname,rownum)

	if str0.find(strname)== -1 :
#		print('True')
		return False
	else :
#		print('False')
		return True
#3.循环查找，然后打印某行

str1=input("check in you want find strings: ")
n=0

while n<rowsum:
	count1 = linecache.getline(logcatname,n)
#	print count
	if seachstr(str1,n)==True:
#		print n
		print(count1)
	n=n+1
