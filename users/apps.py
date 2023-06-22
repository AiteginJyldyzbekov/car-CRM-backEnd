from django.apps import AppConfig

class DriversConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    default_app_config = 'users.apps.YourAppConfig'

    def ready(self):
        import users.signals

    