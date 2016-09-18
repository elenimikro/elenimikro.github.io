#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = u'mikrohelen'
SITENAME = u'mikrohelen'
SITESUBTITLE = u"Eleni Mikroyannidi's personal space"
# SITEURL = 'mikrohelen.com'
SITEURL = 'https://elenimikro.github.io/'

GITHUB_URL = 'https://github.com/elenimikro/elenimikro.github.io/'
TWITTER_USERNAME = 'mikrohelen'

THEME = 'themes/pure-single'
TAGLINE = SITESUBTITLE
COVER_IMG_URL = '/assets/cover_photo.jpg'
PROFILE_IMG_URL = '/assets/mikrohelen_southpark.jpg'

PATH = 'content'
# PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'assets']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['pelican-plugins']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = None

# Markup
TYPOGRIFY = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),
          ('github', 'https://github.com/elenimikro'),
          ('linkedin', 'https://www.linkedin.com/in/elmikro'),
          ('twitter', 'https://twitter.com/mikrohelen'),
          ('rss', '%s/%s' % (SITEURL, FEED_ALL_ATOM)),
          )

DEFAULT_PAGINATION = 10

# default MD_EXTENSIONS setting
MD_EXTENSIONS = ([
    'codehilite(css_class=highlight)',
    'extra',
    'toc'
])
PYGMENTS_STYLE = 'monokai'
MD_EXTENSIONS = ([
    'codehilite(css_class=highlight)',
    'extra',
    'toc',
])

#setup theme:
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Home', '/'),
             ('About', '/about/'),
             ]

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
# DEFAULT_METADATA = (
#     ('Authors', 'Eleni Mikroyannidi')
#     # ('Date', datetime.date.today()),
# )

#clean URLs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Extract a post's date from the filename:
DEFAULT_DATE = 'fs'
WITH_FUTURE_DATES = True




DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
