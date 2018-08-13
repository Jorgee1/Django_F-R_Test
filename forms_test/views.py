from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .serializers import *
from .models import *
import random
import string
from .filters import UserFilter
""" Credenciales Usuarios
	bclayillu
	QD6u03NpKpP


	mmcgrorty1r
	eGPQD75T
"""

def loginView(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = loginForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:
					login(request, user)
					return HttpResponseRedirect('home/')
				else:
					return render(request, "forms_test/login.html", {'form': form, 'error': 'Not a User'})
		else:
			form = loginForm()

		return render(request, "forms_test/login.html", {'form': form})
	else:
		return HttpResponseRedirect('home/')

def signupView(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = signupForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				user = User.objects.create_user(**form.cleaned_data)
				login(request, user)
				return HttpResponseRedirect('home/')
		else:
			form = signupForm()

		return render(request, "forms_test/signup.html", {'form': form})
	else:
		return HttpResponseRedirect('home/')

def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/')

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
		return render(request, 'forms_test/base_profile.html', {'user': request.user, 'form':form})

def homePage(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		print(request.user)
		return render(request, 'forms_test/base_index.html', {'user':request.user})

def ranchView(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		creatures = Creature.objects.filter(owner__pk=request.user.id)
		return render(request, 'forms_test/base_ranch.html', {'user':request.user,'creatures':creatures})

def addCrature(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		user = User.objects.get(pk=request.user.id)
		races = BaseCreature.objects.all()
		id = random.randint(1,races.count())
		creature = Creature(name=''.join(random.choice(string.ascii_letters) for m in range(10)), race=races[id], owner=user )
		creature.save()
		return HttpResponse('<a href="/home/">HOME</a> <div>' + creature.name + ' added</div>')

def queryUsers(request):
    if not request.user.is_authenticated:
        return render(request, 'forms_test/login_error.html')
    else:
        if request.method == 'POST':
            print(request.POST)
            form = searchUser(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                users = UserFilter(form.cleaned_data, queryset=User.objects.all())
                print(users.qs)
                #users = User.objects.filter(username__icontains=form.cleaned_data['username'])
                
                return render(request, 'forms_test/base_search_user.html', {'form': form, 'users': users})

        form = searchUser()
        return render(request, 'forms_test/base_search_user.html', {'form': form})

