LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(module)s %(asctime)s %(pathname)s%(message)s"
        },
    },
    "handlers": {
        # ins django_log file kommen generell nur mindestens warnings
        "django_log": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "django_errors.log",
            "formatter": "simple",
        },
        # Auf die console können wir auch Infos schreiben
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO",
        },
    },
    "root": {"handlers": ["console"], "level": "WARNING"},
    # um doppeltes Loggen mit dem Root Logger zu vermeiden, setzen wir
    "loggers": {
        "django": {
            "handlers": ["django_log", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "eventmanager.events": {
            "handlers": ["django_log"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}
