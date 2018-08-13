from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	city          = serializers.StringRelatedField()
	color         = serializers.StringRelatedField()
	languaje      = serializers.StringRelatedField()
	favorite_food = serializers.StringRelatedField()
	class Meta:
		model = Person
		fields = ('first_name', 'last_name', 'email', 'gender', 'city', 'color', 'languaje', 'favorite_food')