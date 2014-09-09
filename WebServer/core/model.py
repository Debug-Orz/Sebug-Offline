#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
from settings import *


def get_vuln(ssvid):
    rowsN = db.select('sebug_vuln',
                      what='count(*)',
                      where='ssvid = %d' % int(ssvid))[0]['count(*)']

    if rowsN > 0:
        data = db.select('sebug_vuln',
                         where='ssvid = %d' % int(ssvid))
    else:
        data = None

    return data

def get_search(keyword, page):
    rowsN = db.select('sebug_vuln',
                        what='count(*)',
                        where='title LIKE "%%%s%%"' % str(keyword))[0]['count(*)']
    if rowsN > 0:
        data = db.select('sebug_vuln',
                         where='title LIKE "%%%s%%"' % str(keyword),
                         order='date desc',
                         limit='16',
                         offset=str(16*(int(page)-1)))
        if rowsN % 16 == 0: maxPage = rowsN / 16
        else: maxPage = rowsN / 16 + 1
    else:
        data = None
        maxPage = 0

    return data, maxPage

def get_page(page):
    rowsN = db.select('sebug_vuln',
                        what='count(*)')[0]['count(*)']
    if rowsN > 0:
        data = db.select('sebug_vuln',
                         order='date desc',
                         limit='16',
                         offset=str(16*(int(page)-1)))
        if rowsN % 16 == 0: maxPage = rowsN / 16
        else: maxPage = rowsN / 16 + 1
    else:
        data = None
        maxPage = 0

    return data, maxPage