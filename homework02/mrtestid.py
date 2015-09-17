#!/usr/bin/env monkeyrunner
# encoding=utf-8

#MonkeyRunner.py
#导入包和类
import sys
import time
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
#from com.android.hierarchyviewerlib.device import ViewNode
from com.android.hierarchyviewerlib.models import ViewNode
#这个函数时确认年月日时分秒
now=time.strftime("%Y-%m-%d-%H-%M-%S")
#指定我们要保存图片的位置和打印log的位置
path='C:\\pic\\'
logpath="C:\\log\\"

#python中获取当前运行的文件的名字
name=sys.argv[0].split("\\")
filename=name[len(name)-1]

#新建一个log文件
log=open(logpath+filename[0:-3]+"-log"+now+".txt",'w')
#连接设备，两个参数分别是等待的时间(这里的时间都是秒为单位)，设备的序列号。169.254.105.102:5555    device
device=MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device)
#启动activity
device.startActivity(component='com.android.calculator2/.Calculator')
MonkeyRunner.sleep(3)

#通过坐标执行1+2并截图
#device.touch(156,1354,'DOWN_AND_UP')
easy_device.touch(By.id('id/digit1'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
result1=device.takeSnapshot()
result1.writeToFile(path+"button-1"+'.png','png')

#device.touch(900,1604,'DOWN_AND_UP')
easy_device.touch(By.id('id/plus'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
result2=device.takeSnapshot()
result2.writeToFile(path+"button-add"+'.png','png')

#device.touch(396,1354,'DOWN_AND_UP')
easy_device.touch(By.id('id/digit2'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
result3=device.takeSnapshot()
result3.writeToFile(path+"button-2"+'.png','png')

#device.touch(636,1593,'DOWN_AND_UP')
easy_device.touch(By.id('id/equal'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
result4=device.takeSnapshot()
result4.writeToFile(path+"button-eq"+'.png','png')
#判断每一部的操作正确性
result1True=MonkeyRunner.loadImageFromFile('C:\\picture\\1.png')
if(result1.sameAs(result1True,0.9)):
    #在命令行打印出信息
    print("touch 1 succeed")
    #打印信息到log文件
    log.write("touch 1 succeed……\n")
else:
    #打印信息到命令行
    print("touch 1 failed")
    log.write("touch 1 failed……\n")

result2True=MonkeyRunner.loadImageFromFile('C:\\picture\\add.png')
if(result2.sameAs(result2True,0.9)):
    #在命令行打印出信息
    print("touch add succeed")
    #打印信息到log文件
    log.write("touch add succeed……\n")
else:
    #打印信息到命令行
    print("touch add failed")
    log.write("touch add failed……\n")

result3True=MonkeyRunner.loadImageFromFile('C:\\picture\\2.png')
if(result3.sameAs(result3True,0.9)):
    #在命令行打印出信息
    print("touch 2 succeed")
    #打印信息到log文件
    log.write("touch 2 succeed……\n")
else:
    #打印信息到命令行
    print("touch 2 failed")
    log.write("touch 2 failed……\n")
	
result4True=MonkeyRunner.loadImageFromFile('C:\\picture\\eq.png')
if(result4.sameAs(result4True,0.9)):
    #在命令行打印出信息
    print("touch eq succeed")
    #打印信息到log文件
    log.write("touch eq succeed……\n")
else:
    #打印信息到命令行
    print("touch eq failed")
    log.write("touch eq failed……\n")

#通过ID执行1+2并断言每一部操作
