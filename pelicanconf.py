AUTHOR = "Alexey"
SITENAME = "b00bl1k's homepage"
SITEURL = "http://127.0.0.1:8000"
PATH = "content"
THEME = "theme"
TIMEZONE = "Europe/Moscow"
DEFAULT_LANG = "en"
FEED_ALL_ATOM = "feed.xml"
TRANSLATION_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
DIRECT_TEMPLATES = ["index"]
STATIC_PATHS = ["assets"]
SOCIAL = (
    ("email", "6006l1k@gmail.com", "mailto:6006l1k@gmail.com"),
    ("github", "b00bl1k", "https://github.com/b00bl1k"),
    ("fediverse", "@b00bl1k@lor.sh", "https://lor.sh/@b00bl1k"),
)
PLUGINS = ["webassets"]
DEFAULT_PAGINATION = None
RELATIVE_URLS = False
SOURCE_CODE_URL = "https://github.com/b00bl1k/b00bl1k.ru"
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{path_no_ext}.html"
DESCRIPTION = ""
