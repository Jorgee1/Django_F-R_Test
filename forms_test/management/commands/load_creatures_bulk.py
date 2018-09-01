from django.core.management.base import BaseCommand
from django.core.management import call_command
from itertools import islice

import csv
from forms_test.models import *

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	batch_size = 100

	def handle(self, *args, **options):
		BaseCreature.objects.all().delete()
		with open('data_set/creatureDB.csv', encoding="latin1") as db:
			data = csv.DictReader(db)

			while True:
				obj = []
				batch = list(islice(data, self.batch_size))

				if not batch:
					break

				for i in batch:
					obj.append(BaseCreature(**i))


				BaseCreature.objects.bulk_create(obj, self.batch_size)


		print("DONE")
