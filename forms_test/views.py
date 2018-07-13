from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .serializers import *
from .models import *

def loginView(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = loginForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:
					login(request, user)
					return HttpResponseRedirect('/forms/home/')
				else:
					return render(request, "forms_test/login.html", {'form': form, 'error': 'Not a User'})
		else:
			form = loginForm()

		return render(request, "forms_test/login.html", {'form': form})
	else:
		return HttpResponseRedirect('/forms/home/')

def signupView(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = signupForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				user = User.objects.create_user(**form.cleaned_data)
				login(request, user)
				return HttpResponseRedirect('/forms/home/')
		else:
			form = signupForm()

		return render(request, "forms_test/signup.html", {'form': form})
	else:
		return HttpResponseRedirect('/forms/home/')

def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/forms/')

def profileView(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		user = User.objects.get(pk=request.user.id)
		if request.method == 'POST':
			form = profileForm(request.POST)
			if form.is_valid():
				user.email      = form.cleaned_data['email']
				user.first_name = form.cleaned_data['first_name']
				user.last_name  = form.cleaned_data['last_name']
				user.save()
		print(UserSerializer(user).data)
		form = profileForm(UserSerializer(user).data)
		return render(request, 'forms_test/profile.html', {'user': request.user, 'form':form})

def homePage(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		print(request.user)
		return render(request, 'forms_test/index.html', {'user':request.user})

def ranchView(request):
	creatures = Creature.objects.filter(owner__pk=request.user.id)
	print(creatures)
	return render(request, 'forms_test/ranch.html', {'user':request.user,'creatures':creatures})
