# -*- coding: utf-8 -*-
#读logcat文件
#查找某个字符并打印该行
import os
import sys
import datetime,time
import linecache

logcatfilepath=''
logname=''
#1.获取文件行号
def filerowsum(logname):
	rowsum=len(open(logcatfilepath,logname).readlines())
	return rowsum
#2.查找每一行是否有字符
def seachstr(strname,rownum):
	str1= linecache.getline(logname,rowsum)
	if str1.find(strname)!=null:
		return True
	else :
		return False
#3.循环查找，然后打印某行
n=0
while n<rowsum:
	count = linecache.getline(filename,linenum)
	if seachstr(count,n)=True:
		print count
	n=n+1
