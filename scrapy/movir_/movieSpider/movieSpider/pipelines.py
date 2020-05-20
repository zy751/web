# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .settings import STR
import pymysql

class MoviespiderPipeline(object):
    def process_item(self, item, spider):
        return item
class mysqlPipline(object):
    def __init__(self):
        self.conn=pymysql.Connect(host='localhost',port=3306,user='root',password='root',db='django_blog',charset='utf8')
        self.cusor=self.conn.cursor()
        if STR=='1':
            self.TAB='users_movie'
        if STR=='2':
            self.TAB='users_sitcom'
        if STR=='3':
            self.TAB='users_variety'
        if STR=='4':
            self.TAB='users_comic'
    def process_item(self,item,spider):
        sql=f'insert into {self.TAB}(title,href,imgsrc,author,pers,area,year,mes) values (%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cusor.execute(sql,(item['title'],item['href'],item['imgsrc'],item['author'],item['pers'],item['area'],item['year'],item['mes']))
        self.conn.commit()
        return  item
    def spider_close(self):
        self.cusor.close()
        self.conn.close()
