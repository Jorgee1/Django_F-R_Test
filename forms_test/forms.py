from django import forms

# https://stackoverflow.com/questions/47120069/django-load-currently-logged-in-user-information-in-the-form
class loginForm(forms.Form):
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(label='password', widget=forms.PasswordInput, max_length=100)

class signupForm(forms.Form):
	username   = forms.CharField(label='username', required=True, max_length=100)
	password   = forms.CharField(label='password', required=True, widget=forms.PasswordInput, max_length=100)
	first_name = forms.CharField(label="first name", required=True, max_length=100)
	last_name  = forms.CharField(label="last name", required=True, max_length=100)
	email      = forms.EmailField(label='email', required=True)

class profileForm(forms.Form):
	first_name = forms.CharField(label="first name", required=True, max_length=100)
	last_name  = forms.CharField(label="last name", required=True, max_length=100)
	email      = forms.EmailField(label='email', required=True)
