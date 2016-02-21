from django.contrib import admin

# Register your models here.

from todos.models import UserProfile #, tasks, othermodel, model4

admin.site.register(UserProfile)