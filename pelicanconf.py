# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ankur Sinha'
SITENAME = u'ankursinha.in/blog'
SITESUBTITLE = u'neuroscience/fedora/musings ...'
SITETAG = u'neuroscience/fedora/musings ...'
#SITEURL = 'http://ankursinha.in/blog/'
TWITTER_USERNAME = 'sanjay_ankur'

STATIC_PATHS = ['images']
ARTICLE_PATHS = ['']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%b}/{date:%d}/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_aS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

SIDEBAR = 'sidebar.html'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

THEME = 'voidy-bootstrap'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['post_stats', 'render_math', 'sitemap']


# Blogroll
LINKS =  (('Fedora', 'http://fedoraproject.org'),)

# Social widget
SOCIAL = (('Google+', 'https://plus.google.com/105107988864522484597/about',
           'fa fa-google-plus-square fa-fw fa-lg'),
          ('Twitter', 'https://twitter.com/sanjay_ankur',
           'fa fa-twitter-square fa-fw fa-lg'),
          ('Facebook', 'http://www.facebook.com/sanjay.ankur',
           'fa fa-facebook-square fa-fw fa-lg'),
          ('GitHub', 'http://github.com/sanjayankur31',
           'fa fa-github-square fa-fw fa-lg'),
          )

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

CUSTOM_ARTICLE_FOOTERS = ('sharing.html',)
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
