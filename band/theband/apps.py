from django.apps import AppConfig

class ThebandConfig(AppConfig):
    """
    Configuration for the 'theband' application.

    This class is used by Django to configure settings for the 'theband' app,
    including specifying the name of the app and the default type for auto-generated fields.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theband'
