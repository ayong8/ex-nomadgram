from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'nomadgram.images'

    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
