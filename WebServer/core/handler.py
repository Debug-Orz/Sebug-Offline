#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
from setting import *
from model import *

class BaseHandler:
    def __init__(self):
        pass


class IndexHandler(BaseHandler):
    def GET(self):
        return render.index()


class SearchHandler(BaseHandler):
    def GET(self, key):
        data = get_search(key)
        if data is None:
            return render.error()
        return render.search(key, data)


class PageHandler(BaseHandler):
    def GET(self, page):
        data = get_page(page)
        if data is None:
            return render.error()
        return render.page(page, data)


class ViewHandler(BaseHandler):
    def GET(self, ssvid):
        data = get_vuln(ssvid)
        if data is None:
            return render.error()

        return render.error()
