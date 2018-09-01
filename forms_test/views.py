from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *
import random
import string
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
					return HttpResponseRedirect('/home/')
				else:
					return render(request, "login/base_login.html", {'form': form, 'error': 'Not a User'})
		else:
			form = loginForm()

		return render(request, "login/base_login.html", {'form': form})
	else:
		return HttpResponseRedirect('/home/')

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

		return render(request, "login/base_signup.html", {'form': form})
	else:
		return HttpResponseRedirect('home/')

def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def profileView(request):
	user = User.objects.get(pk=request.user.id)
	if request.method == 'POST':
		form = profileForm(request.POST)
		if form.is_valid():
			user.email      = form.cleaned_data['email']
			user.first_name = form.cleaned_data['first_name']
			user.last_name  = form.cleaned_data['last_name']
			user.save()

	form = profileForm({'first_name':user.first_name,'last_name':user.last_name,'email':user.email})
	return render(request, 'main/base_profile.html', {'user': request.user, 'form':form})

@login_required
def homePage(request):
	print(request.user)
	return render(request, 'main/base_index.html', {'user':request.user})

@login_required
def ranchView(request):
	creatures = Creature.objects.filter(owner__pk=request.user.id)
	return render(request, 'main/base_ranch.html', {'user':request.user,'creatures':creatures})

@login_required
def addCrature(request):
	user = User.objects.get(pk=request.user.id)
	races = BaseCreature.objects.all()
	id = random.randint(1,races.count())
	creature = Creature(name=''.join(random.choice(string.ascii_letters) for m in range(10)), race=races[id], owner=user )
	creature.save()
	return HttpResponse('<a href="/ranch/">Ranch</a> <div>' + creature.name + ' added</div>')

@login_required
def queryUsers(request):
    if request.method == 'POST':
        print(request.POST)
        form = searchUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            users = UserFilter(form.cleaned_data, queryset=User.objects.all())
            print(users.qs)
            #users = User.objects.filter(username__icontains=form.cleaned_data['username'])
            
            return render(request, 'main/base_search_user.html', {'form': form, 'users': users})

    form = searchUser()
    return render(request, 'main/base_search_user.html', {'form': form})

