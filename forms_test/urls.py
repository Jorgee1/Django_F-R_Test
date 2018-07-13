from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.loginView),
    path('signup/', views.signupView),
    path('home/', views.homePage),
    path('logout/', views.logoutView),
    path('profile/', views.profileView),
    path('ranch/', views.ranchView),
]
