from django.core.management.base import BaseCommand
from django.core.management import call_command

import csv
from forms_test.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        with open('data_set/creatureDB.csv', encoding="latin1") as db:
            data = csv.DictReader(db)
            for creature in data:
                print(creature)
                creatureObj = BaseCreature(**creature)
                creatureObj.save()
        print("DONE")
