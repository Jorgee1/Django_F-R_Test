from django.core.management.base import BaseCommand
from django.core.management import call_command

import csv
from main.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        City.objects.all().delete()
        Color.objects.all().delete()
        Languaje.objects.all().delete()
        Person.objects.all().delete()

        with open('data_set/MOCK_DATA.csv', encoding="latin1") as db:
            data = csv.DictReader(db)
            for i in data:
                print(i)

                city = City.objects.filter(name=i['city'])

                if not city.exists():
                    city = City(name=i['city'])
                    city.save()
                else:
                    city = city.first()

                color = Color.objects.filter(name=i['color'])
                if not color.exists():
                    color = Color(name=i['color'])
                    color.save()
                else:
                    color = color.first()

                languaje = Languaje.objects.filter(name=i['languaje'])
                if not languaje.exists():
                    languaje = Languaje(name=i['languaje'])
                    languaje.save()
                else:
                    languaje = languaje.first()

                person = Person(person_id=i["id"], first_name=i["first_name"],
                                last_name=i["last_name"], email=i["email"],
                                favorite_food=i["favorite_food"])
                person.save()

                person.city     = city
                person.color    = color
                person.languaje = languaje

                if i["gender"] == "Male":
                    person.gender = Person.MALE
                else:
                    person.gender = Person.FEMALE

                person.save()

        print("DONE")
