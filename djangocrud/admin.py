from django.contrib import admin
from .models import CreateTask, Categories
from Users.models import  LibraryCategory


admin.site.register(CreateTask)
admin.site.register(Categories)
admin.site.register(LibraryCategory)

