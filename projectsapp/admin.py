from projectsDB.projectsapp.views import ProjectsView
from django.contrib import admin
from .models import Projects

# Register your models here.
admin.site.register(Projects)