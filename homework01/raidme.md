此次作业以greenvpn客户端为主要对象
adb
1. 使用genymotion安装一个应用；
adb install packagename
在虚拟机上安装qq、微信等常见应用时，出现错误。
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb1.PNG)

2. 查看应用的package name；
/data/data/目录下查看文件夹名，这里存放了已安装的app
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb2-1.PNG)

启动app，通过ps，查看进程，进程名也是packagename
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb2-2.PNG)

3. 将电脑里一个文件放到这个应用的某个目录内；
adb push ~/pc文件 /android文件夹/
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb3-1.PNG)
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb3-2.PNG)

4. 查看该应用是否有本地的共享文件或者db。
/data/data/目录下，进入应用对应的目录，就可以查看相应的文件，在这里发现，greenvpn的账号和密码都是明文
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb3.PNG)
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/adb4-ming.PNG)

ddms
1.查看应用的package name；
device中，可以查看到正在运行的app的包名；logcat中，通过activitymanage也可以看到包名和activity名
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/ddms1-1.PNG)
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/ddms1-2.PNG)

2.查看应用某个场景的内存增长以及峰值；
在device中，选择某个进程，单击show heap updates，在VM Heap栏，单击Cause GC,即可查看内存的使用情况。
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/ddms2-1.PNG)

3.增加一个过滤的条件来查看应用的log。
logcat点“+”号，就能添加日志过滤条件
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/ddms3-1.PNG)

hierarchyviewer
1.查看应用的某界面结构图；
E:\Android\adt\sdk\tools下的hierarchyviewer.bat启动hierarchyviewer
接上设备后，会记录下设备的界面变化情况，点击load view hierarchy可以查看界面结果详情
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/hierarchyviewer1.PNG)
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/hierarchyviewer3.PNG)
2.查看应用的控件的绘制性能。
在switch to the tree view下选中一个view，点击profile node就可以查看各个view的绘制时间。
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework01/hierarchyviewer2.PNG)
