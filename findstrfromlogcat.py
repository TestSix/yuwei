# -*- coding: utf-8 -*-
#读logcat文件
#查找某个字符并打印该行
import os
import sys
import datetime,time
import linecache

logcatfilepath = os.path.split(os.path.realpath(__file__))[0]
logcatname=logcatfilepath+'\\logcat.log'
#1.获取文件行号
def filerowsum(logname):
	rowsum=len(open(logcatname,'rU').readlines())
	return rowsum
#2.查找每一行是否有字符
def seachstr(strname,rownum):
	str1= linecache.getline(logcatname,rownum)
	
	if str1.find(strname)!=null :
		print('True')
		return True
	else :
		print('False')
		return False
#3.循环查找，然后打印某行
#str1=input()
str1='activity'
n=0
rSum=filerowsum(logcatname)
while n<rSum:
	count = linecache.getline(logcatname,n)
	print count
	if seachstr(str1,n)==True:
		print n
		print count
	n=n+1
