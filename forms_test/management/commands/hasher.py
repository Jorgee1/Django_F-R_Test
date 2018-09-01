from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.hashers import make_password

from os import path
import csv


class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'


	def handle(self, *args, **options):
		root = 'data_set'
		with open(path.join(root, 'Users-notHashed.csv')) as user_source,\
				open(path.join(root, 'Users.csv'), 'w') as user_destination:

			users_data_source = csv.DictReader(user_source)
			users_data_destination = csv.DictWriter(user_destination, users_data_source.fieldnames)
			users_data_destination.writeheader()
			
			for index, user in enumerate(users_data_source):

				user['password'] = make_password(user['password'])
				users_data_destination.writerow(user)
				print('Progress:', (index/1000)*100, '%', 'user', user['username'])
