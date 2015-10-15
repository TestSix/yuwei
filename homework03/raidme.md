Charles证书的安装：
![image](https://github.com/TestSix/yuwei/blob/master/homework03/crtinstall.png)
只需要在Charles官网下载，然后双击安装即可，注意修改成‘始终信任’

http的抓包结果如下：
![image](https://github.com/TestSix/yuwei/blob/master/homework03/http1.PNG)
![image](https://github.com/TestSix/yuwei/blob/master/homework03/http2.PNG)
![image](https://github.com/TestSix/yuwei/blob/master/homework03/http3.PNG)
http的包可以看到request和response的内容。

https的抓包结果如下：
![image](https://github.com/TestSix/yuwei/blob/master/homework03/https1.PNG)
![image](https://github.com/TestSix/yuwei/blob/master/homework03/https2.PNG)
![image](https://github.com/TestSix/yuwei/blob/master/homework03/https3.PNG)
![image](https://github.com/TestSix/yuwei/blob/master/homework03/https4.PNG)
![image](https://github.com/TestSix/yuwei/blob/master/homework03/crtinstall.PNG)
https的包则显示unknown，有request内容，但没有response内容。

由于公司没有https的代理服务器，没有完成对应被测应用的证书抓取。


参考资料：
唐巧的技术博客-iOS开发工具-网络封包分析工具Charles
http://blog.devtang.com/blog/2013/12/11/network-tool-charles-intr/
android开发中监控android软件网络请求的软件Charles使用入门
http://www.cnblogs.com/cerxp/p/3531766.html
Android单元测试初探——Instrumentation
http://www.oschina.net/question/54100_27061
