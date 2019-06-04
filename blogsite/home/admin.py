from django.contrib import admin
from home.models import Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
