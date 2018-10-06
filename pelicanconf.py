#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Mesejo'
SITENAME = 'The Fox Den'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'mesejoleon@gmail.com'),
          ('twitter', 'https://twitter.com/mesejo410'),
          ('linkedin', 'https://www.linkedin.com/in/daniel-alejandro-mesejo-le%C3%B3n/'),
          ('github', 'https://github.com/mesejo'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']

THEME = "../pelican-themes/hyde"

BIO = "I'm Daniel Mesejo-Leon, from La Habana. Living and working in Rio de Janeiro. Trying to become a Software Engineer"
PROFILE_IMAGE = "avatar.jpg"
