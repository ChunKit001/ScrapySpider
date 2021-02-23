#对python爬虫框架scrapy的一个简单封装 
对于编写新的爬虫可直接使用此模块替换默认的框架生成的代码  
进行了基本的反反爬设置  
主要包括了随机UA和随机代理  
基于python3.7和scrapy2.4.4**开发

##依赖安装
pip install scrapy  
pip install scrapy-fake-useragent  
pip install scrapy-proxies-tool

###使用anaconda替代python3的用户在win下可能需要
pip install -I cryptography --user

###安装scrapy可能需要
下载twisted(对应python版本和windows位)  
https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted  
打开下载路径 并执行  
pip install 文件名

###爬取ip池使用ipproxy-docker镜像
docker run -p 8000:8000 cz5424/ipproxypool

##测试爬虫
执行test.py即可

##其他资料
https://hub.docker.com/r/cz5424/ipproxypool  
https://pypi.org/project/scrapy-fake-useragent/  
https://pypi.org/project/scrapy-proxies-tool/  
https://www.cnblogs.com/qiyeboy/p/5693128.html  