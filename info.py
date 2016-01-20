# import re,urllib,socket,os,datetime,sys,time
# string = "http://www.chinanews.com/gn/2016/01-20/7724095.shtml";

# string_split = string.split("/")
# print string_split[3]

import sqlite3
# Write Sqlites3
con = sqlite3.connect("development.sqlite3")
cu = con.cursor()
# cu_url = newsUrl.strip().split("/")
# cu_info = cu_url[3].strip()
# print cu_info
newsTitle = 'test1'
strText = 'test1'
cu_info = 'test1'
newsTime = '2015-12-13'
con.execute("insert into articles(title,text,author_id,info,created_at,updated_at) values('"+newsTitle+"','"+strText+"',1,'"+cu_info+"','"+newsTime+"','"+newsTime+"')")
# con.execute("insert into articles(title,text,author_id,info,created_at,updated_at) values('test','test',1,'test','2015-12-12','2015-12-13')")
# print cu_info
con.commit()
con.close()