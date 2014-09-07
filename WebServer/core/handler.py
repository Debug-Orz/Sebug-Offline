#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
from setting import *
from model import *
from HTMLParser import HTMLParser

class BaseHandler:
    def __init__(self):
        pass


class IndexHandler(BaseHandler):
    def GET(self):
        return render.index()


class SearchHandler(BaseHandler):
    def GET(self, keyword, page=1):
        data, maxPage = get_search(keyword, page)
        if data is None:
            return render.error()
        return render.search(keyword, data, page, maxPage)


class PageHandler(BaseHandler):
    def GET(self, page):
        data, maxPage = get_page(page)
        if data is None:
            return render.error()
        return render.page(data, page, maxPage)


class ViewHandler(BaseHandler):
    def GET(self, ssvid):
        data = get_vuln(ssvid)
        if data is not None:
            return render.view(data)
        return render.error()
