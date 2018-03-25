#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://ankursinha.in'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/categories/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/categories/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'
TAG_FEED_RSS = 'feeds/tags/%s.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/authors/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/authors/%s.rss.xml'
FEED_MAX_ITEMS = 10

DELETE_OUTPUT_DIRECTORY = False

DISQUS_SITENAME = u'ankursinha'
GOOGLE_ANALYTICS = "UA-60261100-1"
