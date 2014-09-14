#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'RickGray'
from core.settings import *
from core.urls import *
from core.handler import *

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
