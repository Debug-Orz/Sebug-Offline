#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
import web


sqlite_path = 'sebug.db'  # db file path

web.config.debug = True  # debug on/off

db = web.database(dbn='sqlite', db=sqlite_path)

render = web.template.render('templates', base='base')  # template