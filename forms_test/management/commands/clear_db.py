from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.apps import apps
import csv
from forms_test.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        app_models = apps.get_app_config('forms_test').get_models()
        for model in app_models:
            model.objects.all().delete()

        print("DONE")