# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ankur Sinha'
SITENAME = u'ankursinha.in/blog'
SITESUBTITLE = u'neuroscience/fedora/musings ...'
SITETAG = u'neuroscience/fedora/musings ...'
#SITEURL = 'http://ankursinha.in/blog/'
TWITTER_USERNAME = 'sanjay_ankur'

STATIC_PATHS = ['images', 'extras/favicon.ico']
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path':'favicon.ico'}
}
ARTICLE_PATHS = ['']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_aS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

SIDEBAR = 'sidebar.html'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

THEME = 'voidy-bootstrap'

PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['post_stats', 'render_math', 'sitemap', 'better_figures_and_images']
#RESPONSIVE_IMAGES = False
PLUGINS = ['post_stats', 'render_math', 'sitemap', 'tag_cloud',]

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 30
TAG_CLOUD_SORTING = 'random'


# Blogroll
LINKS =  (('UH Biocomputation', 'http://homepages.stca.herts.ac.uk/~nngroup/index.php'),
          ('OCNS', 'https://ocns.memberclicks.net/'),
          ('Fedora Project', 'http://fedoraproject.org'),
          ('All Feeds', 'http://ankursinha.in/blog/feeds/'),)

# Social widget
SOCIAL = (('Goodreads', 'https://www.goodreads.com/user/show/32360473-ankur',
           'fa fa-book fa-fw fa-lg'),
          ('Scholar', 'http://scholar.google.co.in/citations?user=919ScZEAAAAJ&hl=en',
           'fa fa-google fa-fw fa-lg'),
          ('Google+', 'https://plus.google.com/105107988864522484597/about',
           'fa fa-google-plus-square fa-fw fa-lg'),
          ('Twitter', 'https://twitter.com/sanjay_ankur',
           'fa fa-twitter-square fa-fw fa-lg'),
          ('Facebook', 'http://www.facebook.com/sanjay.ankur',
           'fa fa-facebook-square fa-fw fa-lg'),
          ('GitHub', 'http://github.com/sanjayankur31',
           'fa fa-github-square fa-fw fa-lg'),
          ('Last.fm', 'http://www.last.fm/user/sanjay_ankur',
           'fa fa-lastfm-square fa-fw fa-lg'),
          ('Foursquare', 'https://foursquare.com/sanjay_ankur/',
           'fa fa-foursquare fa-fw fa-lg'),
          ('Flickr', 'https://www.flickr.com/people/30402562@N07/',
           'fa fa-flickr fa-fw fa-lg'),
          ('Instagram', 'https://instagram.com/sanjay.ankur/',
           'fa fa-instagram fa-fw fa-lg'),
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

STYLESHEET_FILES = ("use-opensans.css", "voidybootstrap.css", "pygment.css")
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
