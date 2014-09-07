#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
import web

sqlite_path = 'sebug.db'
web.config.debug = True
db = web.database(dbn='sqlite', db=sqlite_path)
render = web.template.render('templates')