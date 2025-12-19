AUTHOR = 'MasudaYouichi'
SITENAME = 'Handicraft'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# テーマを設定
THEME = 'theme/elegant'


# プラグイン
PLUGINS = ['pelican.plugins.sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities':{
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
        },
    'changefreqs':{
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
        }
    
    }

# robot.txt
STATIC_PATH = ['images','robots.txt']
EXTRA_PATH_METADATA = {
    'robots.txt':{'path':'robots.txt'},
    }
