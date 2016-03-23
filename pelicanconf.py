#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gavin Lin'
SITENAME = u"Gavin's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = (('index'))

# Blogroll
LINKS = (('onelong', 'http://ways2u.com/'),
         ('zita', 'http://blog.csdn.net/ttxgz'),)

# Social widget
SOCIAL = (('github', 'https://github.com/gavinlin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME = 'basic'
#THEME = "/Users/gavinlin/workspace/github/blog_source/pixyll"
THEME = "pelican-material"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math', 'sitemap', 'multi_part',  'series']

#sitemap
SITEMAP = {
    'format':'xml',
    'priorities':{
        'articles':0.7,
        'indexes':0.6,
        'pages':0.5
    },
    'changefreqs':{
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

STATIC_PATHS = [
    u'CNAME',
    u'images',
    ]

DISQUS_SITENAME = u'gavincodecom'

MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight)', 'extra']

from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order
