# AUTHOR = 'Kaede Yu, Mike Liu'
SITENAME = 'Collapse of USSR'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# # Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "theme/subtle"
# DEFAULT_DATE = 'fs'
LOAD_CONTENT_CACHE = False
DATE_FORMATS = {
    'en': ('usa','%a, %d %b %Y')
}
LOCALE = ('usa')
# NEWEST_FIRST_ARCHIVES = True
# REVERSE_CATEGORY_ORDER = True
ARTICLE_ORDER_BY = 'date'
PAGE_ORDER_BY = 'date'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False