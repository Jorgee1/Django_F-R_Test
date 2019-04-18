from django.urls import include, path
from .views import *

urlpatterns = [
    path('', loginView, name="login"),
    path('sign_up/', signupView, name="sign_up"),
    path('home/', homeView, name="home"),
    path('logout/', logoutView, name="logout"),
    path('profile/', profileView, name="profile"),
    path('ranch/', ranchView, name="ranch"),
    path('add/', addCrature, name="add_creature"),
    path('users/', queryUsers, name="search_user")
]
