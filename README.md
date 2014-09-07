Sebug-Offline
===

Sebug-Offline是由python2编写的Sebug离线版查询程序（以供一些特殊环境的使用），里面包含了sebug爬虫和WebServer两个子程序。

该程序依赖于``Scrapy``爬虫框架和``web.py``轻量级webserver，你可以在这里查看到这两个项目：

* Scrapy : [http://scrapy.org][href1]
* Web.py: [http://webpy.org][href2]

ScreenShots
----

### Start Page
![][img1]

### Show Page
![][img2]

Installation
----
将此项目克隆至本地：
    
    git clone https://github.com/rickgray/Sebug-Offline.git Sebug-Offline
    
该项目由python2.7.6编写和维护。

Usage
----
进入到Sebug爬虫项目：

    cd SebugSpider
    
启动爬虫开始抓取（前提装好scrapy）：

    scrapy crawl sebug

或者保存爬虫状态至 ``crawls/sebug-1`` 方便暂停和恢复爬虫：

    scrapy crawl sebug -s JOBDIR=crawls/sebug-1
    
爬取完成后，将sebug.db放至WebServer目录下，或者修改 ``core/setting.py`` 数据库文件存放路径，然后运行webserver：

    cd WebServer
    python main.py
    
此时，可以打开浏览器输入 ``http://localhost:8080`` 即可开始本地sebug之旅。
    

[href1]:http://scrapy.org/
[href2]:http://webpy.org/


[img1]:http://rickgray.github.io/Mixed/images/Sebug-Offline/shot1.png
[img2]:http://rickgray.github.io/Mixed/images/Sebug-Offline/shot2.png