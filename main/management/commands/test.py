from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        print("DONE")
