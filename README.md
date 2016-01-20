#News Spider
> Tanks to [getnews][!https://github.com/mankunzhao/getnews.git]

---

##Default Site

* 中国新闻网(ZXW)
* 网易新闻(163)
* 人民网(RMW)
* 新浪(SINA)
* 凤凰资讯(IFENG)

##Configuration

* defaultSiteList = ["ZXW","163","RMW","SINA","IFENG"]
* argD = os.getcwd()+os.path.sep+'dataNews'#directory of news

##Introduction

* python GetChinaNews.py 获取当天新闻（对于163和RMW这个无效，因为它们的滚动新闻页面没有当天的）
* python GetChinaNews.py -d 2013-11-12  获取2013-11-12这一天的新闻
* python GetChinaNews.py -d 2013-11-12 2013-11-14 获取2013-11-12到2013-11-14之间的新闻
* python GetChinaNews.py -dx 2013-11-12 5 获取2013-11-12之后5天的新闻
* python GetChinaNews.py -a 获取最近30天内的新闻
