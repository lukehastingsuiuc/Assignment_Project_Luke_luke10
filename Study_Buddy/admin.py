from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Materials, Assignment
admin.site.register(Materials)
admin.site.register(Assignment)
admin.site.register(User)
