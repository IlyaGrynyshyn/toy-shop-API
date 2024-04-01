import dj_database_url

from toy_shop_api.settings.base import *

DEBUG = False


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
