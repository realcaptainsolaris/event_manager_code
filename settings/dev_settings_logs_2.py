from debug_toolbar.panels.logging import collector

# Einen Handler einrichten, damit die Daten an die Debug-Toolbar gestreamt werden.
LOGGING["handlers"].update({
    "djdt_log": {
        "level": "DEBUG",
        "class": "debug_toolbar.panels.logging.ThreadTrackingHandler",
        "collector": collector,
    },
})

LOGGING["loggers"].update({
    "events": {
        "handlers": ["django_log", "console", "djdt_log"],
        "level": "DEBUG",
        "propagate": False,
    },
    "django": {
        "handlers": ["django_log", "console", "djdt_log"],
        "level": "WARNING",
    },
    # faker spammt die Logs mit Infos beim Testen wegen UserFactory
    "faker": {"level": "ERROR", "propagate": True},
    "factory": {"level": "ERROR", "propagate": True},
})
