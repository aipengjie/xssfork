#! /usr/bin/env python
# coding=utf-8
"""
Copyright (c) 2017 xssfork developers (http://xssfork.codersec.net/)
See the file 'doc/COPYING' for copying permission
"""
import sys

def init_encode():
    reload(sys)
    sys.setdefaultencoding('utf8')


def url_encode(url):
    return url.replace("'", "%27").replace("\"", "%22")