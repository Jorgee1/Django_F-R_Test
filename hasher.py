from django.contrib.auth.hashers import make_password
from os import path
import csv
root = 'data_set'

with open(path.join(root, 'Users-notHashed.csv')) as user_source,\
		open(path.join(root, 'Users.csv'), 'wb') as user_destination:

	users_data_source = csv.DictReader(user_source)
	users_data_destination = csv.DictReader(user_destination)

	for user in users_data_source:
		user['password'] = make_password(user['password'])
		users_data_destination.writerow(user)

