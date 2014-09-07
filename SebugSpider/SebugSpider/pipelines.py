# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class SebugPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('sebug.db')
        self.sqlite3_init()
        # self.cursor = self.conn.cursor()

    def sqlite3_init(self):
        self.conn.execute('''
                create table is not exists sebug_vuln (
                    ssvid integer not null primary key,
                    title longtext not null,
                    date char(40) not null,
                    content longtext not null
                )
            ''')
        self.conn.execute('''
                create index is not exists 'vuln_id'
                    on 'sebug_vuln' ('ssvid')
            ''')

        self.conn.commit()


def process_item(self, item, spider):
    self.conn.execute('''
            insert into sebug_vuln(ssvid, title, date, content) values (?,?,?,?)
        ''', (item['ssvid'], item['title'], item['date'], item['content']))
    self.conn.commit()

    return item
