import random
import string

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from .models import *
from .forms import *
from .filters import UserFilter



def loginView(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = loginForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:
					login(request, user)
					return redirect('home')
				else:
					return render(request, "login.html", {'form': form, 'error': 'Not a User'})
		else:
			form = loginForm()
			return render(request, "login.html", {'form': form})
	else:
		return redirect('home')


def signupView(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = signupForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				user = User.objects.create_user(**form.cleaned_data)
				login(request, user)
				return redirect('home')
		elif request.method == 'GET':
			form = signupForm()
			return render(request, "sign_up.html", {'form': form})
	else:
		return redirect('home')


def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
	
	return redirect('login')


def profileView(request):
	if request.user.is_authenticated:
		user = User.objects.get(pk=request.user.id)
		if request.method == 'POST':
			form = profileForm(request.POST)
			if form.is_valid():
				user.email      = form.cleaned_data['email']
				user.first_name = form.cleaned_data['first_name']
				user.last_name  = form.cleaned_data['last_name']
				user.save()

		form = profileForm({'first_name':user.first_name,'last_name':user.last_name,'email':user.email})
		return render(request, 'profile.html', {'user': request.user, 'form':form})
	else:
		return redirect('login')


def homeView(request):
	if request.user.is_authenticated:
		return render(request, 'home.html', {'user':request.user})
	else:
		return redirect('login')


def ranchView(request):
	if request.user.is_authenticated:
		creatures = Creature.objects.filter(owner__pk=request.user.id)
		return render(request, 'ranch.html', {'user':request.user,'creatures':creatures})
	else:
		return redirect('login')


def addCrature(request):
	if request.user.is_authenticated:
		user = User.objects.get(pk=request.user.id)
		races = BaseCreature.objects.all()
		creature_id = random.randint(1,races.count())
		creature = Creature(name=''.join(random.choice(string.ascii_letters) for m in range(10)), race=races[creature_id], owner=user )
		creature.save()
		return redirect('ranch')
	else:
		return redirect('login')


def queryUsers(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			print(request.POST)
			form = searchUser(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
				users = UserFilter(form.cleaned_data, queryset=User.objects.all())
				print(users.qs)
				#users = User.objects.filter(username__icontains=form.cleaned_data['username'])

				return render(request, 'search_user.html', {'form': form, 'users': users})

		form = searchUser()
		return render(request, 'search_user.html', {'form': form})
	else:
		return redirect('login')

