from django.core.management.base import BaseCommand
from django.core.management import call_command

import csv
from main.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        with open('data_set/MOCK_DATA.csv') as db:
            data = csv.DictReader(db)
            for i in data:
                print(i['city'],",",i["color"],",",i["languaje"])
                temp = City.objects.filter(name=i['city'])
                if temp.exists():
                    print(Exists)
                else:
                    temp = City(name=i['city'])



        print("DONE")
