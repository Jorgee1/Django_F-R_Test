from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

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

def ProfileView(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		form = signupForm({'username':request.user.username})
		print(request.user)
		return render(request, 'forms_test/profile.html', {'user': request.user, 'form':form})

def homePage(request):
	if not request.user.is_authenticated:
		return render(request, 'forms_test/login_error.html')
	else:
		print(request.user)
		return render(request, "forms_test/index.html", {'user':request.user})

