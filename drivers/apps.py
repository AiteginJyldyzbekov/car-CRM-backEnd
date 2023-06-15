from django.apps import AppConfig

class DriversConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drivers'

    default_app_config = 'drivers.apps.YourAppConfig'

    def ready(self):
        import drivers.signals

    