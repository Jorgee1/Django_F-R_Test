from django.contrib import admin
from .models import *


admin.site.register([
    Person,
    Languaje,
    Color,
    City,
])
