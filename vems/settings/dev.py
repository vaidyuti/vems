from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://vems:vems@localhost:5432/vems",
        conn_max_age=600,
    )
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True