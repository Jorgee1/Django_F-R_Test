from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PersonSerializer
from .models import *



def test(request):
	return HttpResponse('{"msg":"HI"}', content_type='application/json')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()[:5]
    serializer_class = PersonSerializer