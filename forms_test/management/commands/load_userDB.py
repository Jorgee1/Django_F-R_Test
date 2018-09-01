from django.core.management.base import BaseCommand
from django.core.management import call_command

import csv
from forms_test.models import *

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def handle(self, *args, **options):
		User.objects.all().exclude(username='kenshinn1').delete()


		with open('data_set/Users.csv', encoding="latin1") as db:
			data = csv.DictReader(db)
			for user in data:
				print(user)
				user = User.objects.create_user(**user)
			print("DONE")

