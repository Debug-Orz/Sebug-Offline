#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
from setting import *


def get_vuln(ssvid):
    data = db.select('sebug_vuln',
                     where='ssvid = %d' % int(ssvid))
    return data

def get_search(key):
    data = db.select('sebug_vuln',
                     where='title LIKE "%%%s%%"' % str(key),
                     order='date desc')
    return data

def get_page(page):
    data = db.select('sebug_vuln',
                     order='date desc',
                     limit='16',
                     offset=str(16*(int(page)-1)))
    return data