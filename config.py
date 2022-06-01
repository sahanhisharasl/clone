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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC7BHar9SqWx4xv2A1k1ifc0eWN0Xe8zin6TuEwyy5rii4b3uJVYOXYhOmM5z3jSWWyG-qMDxmBpIrDa1oK1C3ufAsYWyAjgB9NhDs-Jmqlq88uXNB03tA3F_ccvfA3P7slhpUi-yrVQvIXUJhC6ryqcHL-fSaimLjg6j5PO-RPLm1LuIZB1Vv33m9dUO2b_XR2NorcCtx7nspxJbWlaKIEoYtoLHcLJjWE5qvNveacOPPFCvlfCv3gg8x-Q12VswS2sXwA2CbJfAT8fB_j_Lf8RnM4HJLyjW8bvVEwnF4Q9eOmIibI7sdyFDcdZnwbYXK31AivUWJabn3259EmaACpUFL5gwA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://ejahyeaq:LBYpd8jHPgohAboLRDkvKIbSW_DtQ4e1@rosie.db.elephantsql.com/ejahyeaq")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
