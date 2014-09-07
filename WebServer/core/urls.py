#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'RickGray'
from handler import *

urls = (
    '/', IndexHandler,
    '/page/(\d+)', PageHandler,
    '/search/(.*)', SearchHandler,
    '/vulndb/ssvid/(\d+)', ViewHandler
)