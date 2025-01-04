from django.apps import AppConfig


class HospitalSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital_site'

    def ready(self):
     import hospital_site.translation
