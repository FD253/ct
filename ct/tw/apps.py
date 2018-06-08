from django.apps import AppConfig


class TwConfig(AppConfig):
    name = 'tw'
    def ready(self):
        import tw.signals
