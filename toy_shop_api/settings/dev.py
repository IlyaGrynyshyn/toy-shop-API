from toy_shop_api.settings.base import *

load_dotenv()  # take environment variables from .env.

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
