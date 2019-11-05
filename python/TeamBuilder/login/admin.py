from django.contrib import admin
from .models import Profile, Project, Project_Involved

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Project_Involved)
