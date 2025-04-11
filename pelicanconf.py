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
    ("email", "alex@b00bl1k.ru", "mailto:alex@b00bl1k.ru"),
    ("github", "b00bl1k", "https://github.com/b00bl1k"),
    ("fediverse", "@alex@snac.b00bl1k.ru", "https://snac.b00bl1k.ru/alex"),
)
PLUGINS = ["webassets", "photos"]
DEFAULT_PAGINATION = None
RELATIVE_URLS = False
SOURCE_CODE_URL = "https://github.com/b00bl1k/b00bl1k.ru"
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{path_no_ext}.html"
DESCRIPTION = ""

PHOTO_LIBRARY = "content/galleries"
PHOTO_GALLERY = (1920, 1080, 85)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = True
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = "b00bl1k.ru"
PHOTO_INLINE_ENABLED = True
PHOTO_INLINE_GALLERY_ENABLED = True
