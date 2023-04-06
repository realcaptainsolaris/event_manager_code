from event_manager.settings.base import *

# für Debug-Toolbar
INTERNAL_IPS = ("127.0.0.1",)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MIDDLEWARE.extend(["debug_toolbar.middleware.DebugToolbarMiddleware"])

INSTALLED_APPS.extend(
    [
        "debug_toolbar",
    ]
)


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}
