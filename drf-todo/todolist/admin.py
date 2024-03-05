from django.contrib import admin

# Register your models here.

from todolist.models import Todo


admin.site.register(Todo)
