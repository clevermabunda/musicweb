from django.apps import AppConfig

class UserAuthConfig(AppConfig):
    """
    Configuration for the 'user_auth' application.

    This class is used by Django to configure settings for the 'user_auth' app,
    including specifying the name of the app and the default type for auto-generated fields.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'
