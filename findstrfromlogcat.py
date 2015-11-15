# -*- coding: utf-8 -*-
#读logcat文件
#查找某个字符并打印该行
import os
import sys
import datetime,time
import linecache

logcatfilepath = os.path.split(os.path.realpath(__file__))[0]
logcatname=logcatfilepath+'\\logcat.log'
fileall=linecache.getlines(logcatname)
#1.获取文件行号
#...

rowsum = 0
thefile = open(logcatname, 'rb')
while True:
    buffer = thefile.read(8192*1024)
    if not buffer:
        break
    rowsum += buffer.count('\n')
thefile.close( )
#	return rowsum
#...

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

str1='Activity'
n=0

while n<rowsum:
	count = linecache.getline(logcatname,n)
#	print count
	if seachstr(str1,n)==True:
#		print n
		print count
	n=n+1
