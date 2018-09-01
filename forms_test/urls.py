from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.loginView),
    path('login/', views.loginView),
    path('signup/', views.signupView),
    path('home/', views.homePage),
    path('logout/', views.logoutView),
    path('profile/', views.profileView),
    path('ranch/', views.ranchView),
    path('add/', views.addCrature),
    path('users/', views.queryUsers)
]
