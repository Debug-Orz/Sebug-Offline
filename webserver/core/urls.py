#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'RickGray'

urls = (
    '/', 'IndexHandler',
    '/page/(\d+)', 'PageHandler',
    '/search/(.*)/page/(\d+)', 'SearchHandler',
    '/vulndb/ssvid/(\d+)', 'ViewHandler',
    '/.*', 'ErrorHandler'
)