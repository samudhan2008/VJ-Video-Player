import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'DemoSA')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '27425401'))
API_HASH = environ.get('API_HASH', '36150e358dd8bc2040dc8decd5250bcd')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "7761301018:AAHgMYndGxbU8Efro4smtwklhCffjqE4KPk")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '2107729544'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "7027834290:AAHWkOfvO8nDVrdsqY2H_ogMgKJ8geWeCSI")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002105006808'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://scleechadp:scstream@sc-stream.wptwpvt.mongodb.net/?retryWrites=true&w=majority&appName=sc-stream")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "https://saasdemo.blogspot.com/p/redirect.html")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
