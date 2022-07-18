from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]
SECRET_KEY = ENV_STR("DJANGO_SECRET_KEY", "secret" if DEBUG else "")

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://vems:vems@172.19.0.4:5432/vems",
        conn_max_age=600,
    )
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True