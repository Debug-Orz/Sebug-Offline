#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
from settings import *
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
        elif int(page) > int(maxPage):
            return render.error()
        return render.search(keyword, data, int(page), int(maxPage))


class PageHandler(BaseHandler):
    def GET(self, page):
        data, maxPage = get_page(page)
        if data is None:
            return render.error()
        elif int(page) > int(maxPage):
            return render.error()
        return render.page(data, int(page), int(maxPage))


class ViewHandler(BaseHandler):
    def GET(self, ssvid):
        data = get_vuln(ssvid)
        if data is not None:
            return render.view(data)
        return render.error()


class ErrorHandler(BaseHandler):
    def GET(self):
        return render.error()