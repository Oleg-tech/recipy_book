from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_panel'

    def ready(self):
        from .bot_scheduler import start_polling
        start_polling.start()
