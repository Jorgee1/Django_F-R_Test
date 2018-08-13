<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('forms/', include('forms_test.urls')),
]
=======
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forms_test.urls')),
    path('rest/', include('main.urls')),
]
>>>>>>> 229ac91da66bc26e74ddf0082a096e8de87f0685
