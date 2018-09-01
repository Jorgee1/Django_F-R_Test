from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.hashers import make_password

from itertools import islice

import csv
from forms_test.models import *

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	batch_size = 1000

	def handle(self, *args, **options):
		User.objects.all().delete()
		Profile.objects.all().delete()

		with open('data_set/Users.csv', encoding="latin1") as db:
			data = csv.DictReader(db)
			index = 0
			print('start')
			while True:
				obj = []
				batch = list(islice(data, self.batch_size))
				if not batch:
					break


				for i in batch:
					obj.append(User(**i))

				obj = User.objects.bulk_create(obj, self.batch_size)

				obj_prfile = []

				for i in obj:
					obj_prfile.append(Profile(user=i))


				Profile.objects.bulk_create(obj_prfile, self.batch_size)

				index = index + 1
				print('bulk:', index)

			User.objects.create_superuser('admin', 'admin@example.com', 'admin')
