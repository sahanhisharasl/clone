#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5344936244:AAHl6KS_mI8IOui-y-cRKkw7bGFBK-R04lo")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "5762961"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "c64c435dacb20dd70fa76828c9fd07c5")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1347615107").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BVtsOIIBu7iRsvjngtgRikrnHa244W5z9Xaztu1SZvxhRdQA98PUNs_FCJPkr42oMSxaM6l2JHH3FoW41GhipZ5aTbE_QV8vsINahz6AuykC9RTZYX1UG1pYlr7ISNwRvoBOiRCxikpp6mH7Q9-woU8PBhrEKmb7ntWTw26rpWuUa5aUXTrtIO_CxcjW5DHo-TPaAkI3I0W8vYf8r6ZbP7X3YRAtWR67xY-MI1nc1pk5ErAd0PwpUAFPAW1BQgtbkJDWsfXp60Jh2MsyKPCVCC_L_cjpLMJxB4u9TsB9xfTJovmOHptg13rDi9xT4ry48lPmM3xTOxwkrk8EhKVjCAaycrE5J3s=")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "sqldbtype://slofficial:2004@sahan:5432/new")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
