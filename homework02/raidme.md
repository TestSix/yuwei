Monkey
针对三种不同的场景编写三条不同的命令，并且说明到底是测试什么场景，什么切入点

只有点击操作：
adb shell monkey -p packagename -v -v -v --pct-touch 100 --throttle 500 -s 500 --ignore-crashes --ignor-timeouts 99999

无等待时间的压力测试
adb shell monkey -p packagename -v -v -v --pct-trackball 0 -s 500 --ignore-crashes --ignor-timeouts 99999

与其它应用的影响
adb shell monkey -p packagename1 -p packagename1 -v -v -v --pct-trackball 0 -s 500 --ignore-crashes --ignor-timeouts 99999

MonkeyRunner
编写一条MonkeyRunner的测试用例，可以用原生的坐标API，也可以用扩展的ID定位的API
*扩展ID未完成

执行结果如下：
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework02/rmtest.PNG)

参考：
https://testerhome.com/topics/878

iOS Monkey
执行iOS monkey脚本，github上面随便找一个就可以

执行结果如下：
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework02/crashmonkey4ios1.PNG)
![image](https://raw.githubusercontent.com/TestSix/yuwei/master/homework02/crashmonkey4ios2.PNG)

参考：
https://github.com/vigossjjj/CrashMonkey4IOS
